import unittest
import mock
from entity_extract.extractor.extractors import PosRelationExtractor

from nltk.tree import *


class pos_extractor_test(unittest.TestCase):
    
    def setUp(self):
        self.posExtractor = PosRelationExtractor()
        self.NP = [(1,3,),]
        
    def tearDown(self):
        pass
    
    def test_pos_extract(self):
        pass