import unittest
import mock
from entity_extract.extractor.parsers import base_parser, ChunkParser

from nltk.tree import *


class base_tree_parser(unittest.TestCase):
    
    def setUp(self):
        self.base_tree = base_parser.BaseTreeParser()
        self.sent1 = "(S The/JJ big/JJ orange/NN tiger/NN (RelPhrase (RelP1 (V ran/VBD) (P across/IN)) (RelP2 (V ran/VBD) (P across/IN) )) the/DT green/JJ grass/NN field/NN)"
        
    def tearDown(self):
        pass
    
    @mock.patch('entity_extract.extractor.parsers.base_parser.BaseTreeParser.parse')
    def test_parse_boundaries(self, mock_parse):
        """ Test boundary parse method to see that phrase boundaries are properly
            recorded. 
        """
        
        # We need to create a tree with which to test our parseBoundaries method
        mock_parse.return_value = Tree.fromstring(self.sent1)
        
        # Test specifying a tag type to parse
        bounds = self.base_tree.parseBoundaries(self.sent1, ['RelPhrase','RelP1', 'P'])   
        self.assertEqual(bounds['RelP1'], [(4,6)])
        self.assertEqual(bounds['RelPhrase'], [(4,8)])
        self.assertEqual(bounds['P'], [(5,6), (7,8)])
        
        # Without specifying a tag - all tags should be recorded.
        bounds = self.base_tree.parseBoundaries(self.sent1)   
        self.assertEqual(bounds['RelP1'], [(4,6)])
        self.assertEqual(bounds['RelPhrase'], [(4,8)])
        self.assertEqual(bounds['P'], [(5,6), (7,8)])
        
    
    def test_collapse_boundaries(self):
        """ Test boundary collapse method """
        
        bounds = {'P1' : [(1,3), (3,5), (6,7), (8,12), (9,11), (10, 10)],
                  'P2' : [(1,3), (2,4), (100, 127)]}
        
        # Try while specifying a phrase type to collapse
        cBounds = self.base_tree.collapseBoundaries(bounds, ['P1'])
        
        # Test that P1 was properly collapse
        self.assertEqual(cBounds['P1'], [(1,5), (6,7), (8,12)])
        # P2 should not have been collapsed - so it should the same as above
        self.assertEqual(cBounds['P2'], [(1,3), (2,4), (100, 127)])
        
        # Try without specifying phrase type (should collapse all)
        cBounds = self.base_tree.collapseBoundaries(bounds)
        
        # Test that P1 was properly collapse
        self.assertEqual(cBounds['P1'], [(1,5), (6,7), (8,12)])
        # P2 should nobe collapsed
        self.assertEqual(cBounds['P2'], [(1,4), (100, 127)])
        
        
class chunk_parser_tests(unittest.TestCase):
    
    def setUp(self):
        self.chunkParser = ChunkParser()
        self.parsedSent = [('JJ', u'B-NP'), ('NNP', u'I-NP'), ('VBD', u'O'), ('DT', u'B-NP'), ('NNP', u'I-NP'), ('NNP', u'I-NP'), ('NN', u'I-NP'), ('IN', u'O'), ('NN', u'B-NP'), ('.', u'O')]
        self.rawSent = 'Sean White won the Olympic Gold metal in snowboarding.'
    
    
    def tearDown(self):
        pass
    
    @mock.patch('entity_extract.extractor.parsers.chunk_parser.ChunkParser.parse')
    def test_parse_boundaries(self, mock_parse):
        """ Test boundary parse method for the Chunk Parser """
        
        mock_parse.return_value = self.parsedSent
        
        # Test specifying a phrase type
        bounds = self.chunkParser.parseBoundaries(self.rawSent, ['NP'])
        self.assertEqual(bounds, {'NP' : [(0,2), (3,7), (8,9)]})
        
        # Test without specifying a phrase type
        bounds = self.chunkParser.parseBoundaries(self.rawSent)
        self.assertEqual(bounds, {'NP' : [(0,2), (3,7), (8,9)]})
        
    
    def test_collapse_boundaries(self):
        """ Test Boundary Collapse in Chunk Parser"""
        
        bounds = {'NP' : [(0,2), (3,7), (8,9)]}
        cBounds = self.chunkParser.collapseBoundaries(bounds, 'NP')
        self.assertEqual(bounds, cBounds)
        
        bounds = {'NP' : [(0,2), (2,7), (8,9)]}
        cBounds = self.chunkParser.collapseBoundaries(bounds)
        self.assertEqual(cBounds, {'NP' : [(0,7), (8,9)]})