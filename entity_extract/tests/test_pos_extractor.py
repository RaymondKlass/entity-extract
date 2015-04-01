import unittest
import mock
from entity_extract.extractor.extractors import PosRelationExtractor

from nltk.tree import *


class pos_extractor_test(unittest.TestCase):
    
    def setUp(self):
        self.posExtractor = PosRelationExtractor()
        self.NP = [(1,3,),(7,9,)]
        self.REL = [(5,6,)]
        self.sentence = [('word %s' % i) for i in range(14)]
        
    def tearDown(self):
        pass
    
    def test_pos_extract(self):
        """ Test the part of speech based relation extractor """
        
        extraction = self.posExtractor.extract(self.sentence, self.NP, self.REL)
        self.assertEqual(extraction, [[(1, 3, 'NP', ['word 1', 'word 2']), (5, 6, 'REL', ['word 5']), (7, 9, 'NP', ['word 7', 'word 8'])]])