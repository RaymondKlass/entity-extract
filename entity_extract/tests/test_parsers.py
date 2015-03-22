import unittest
import mock
from entity_extract.extractor.parsers import base_parser

from nltk.tree import *


class base_tree_parser(unittest.TestCase):
    
    def setUp(self):
        self.base_tree = base_parser.BaseTreeParser()
        self.sent1 = "(S The/JJ big/JJ orange/NN tiger/NN (RelPhrase (RelP1 (V ran/VBD) (P across/IN))))"
        
    def tearDown(self):
        pass
    
    @mock.patch('entity_extract.extractor.parsers.base_parser.BaseTreeParser.parse')
    def test_parse_boundaries(self, mock_parse):
        """ Test boundary parse method to see that phrase boundaries are properly
            recorded. 
        """
        
        # We need to create a tree with which to test our parseBoundaries method
        
        
        mock_parse.return_value = Tree.fromstring(self.sent1)
        
        #print self.base_tree.parse('A new sentence')
        bounds = self.base_tree.parseBoundaries('The big orange tiger ran across.', ['RelPhrase','RelP1'])   
        self.assertEqual(bounds['RelP1'], [(4,6)]) 
        self.assertTrue(True)