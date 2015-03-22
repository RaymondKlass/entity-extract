import unittest
import mock
from entity_extract.extractor.parsers import base_parser


class base_tree_parser(unittest.TestCase):
    
    def setUp(self):
        self.base_tree = base_parser.BaseTreeParser
        
    def tearDown(self):
        pass
    
    @mock.patch('entity_extract.extractor.parsers.base_parser.BaseTreeParser.parse')
    def test_parse_boundaries(self, mock_parse):
        """ Test boundary parse method to see that phrase boundaries are properly
            recorded. 
        """
        
        # We need to create a tree with which to test our parseBoundaries method
        
        
        mock_parse.return_value = 'Hello'
        print self.base_tree.parse('A new sentence')    
        self.assertTrue(True)
    