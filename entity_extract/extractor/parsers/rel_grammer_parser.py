# Part of Speach (POS) Based Entity Extraction
# Aimed at Extracting Relationships

# Use regex matching to identify relational phrases
# VP?
# V(W*P)?
# 
# V1: 'RB'
# V2: 'MD', 'VB', 'VBD', 'VBP', 'VBZ', 'VBG', 'VBN'
# V3: 'RP', 'RB'
# (V1)? + (V2) + (V3)?
#
# P1: 'RB'
# P2: 'IN', 'TO', 'RP'
# P3: 'RB'
# (P1)? + (P2) + (P3)?
#
# W: 'PRP$', 'CD', 'DT', 'JJ', 'JJS', 'JJR', 'NN', 'NNS', 'NNP', 'NNPS', 'POS', 'RB', 'RBR', 'RBS', 'VBN', 'VBG'
# (W1)
#

import nltk
from entity_extract.extractor.parsers.base_parser import BaseParser

class RelationGrammerParser(BaseParser):
    
    RelPhraseGrammer = r"""
            V: {<RB>?<MD|VB|VBD|VBP|VBG|VBN><RP|RB>?}
            P: {<RB>?<IN|TO|RP><RB>?}
            RelP1: {(<V><P>?)*}
            RelP2: {(<V>((<PRP$|CD|DT|JJ|JJS|JJR|NN|NNS|NNP|NNPS|POS|RB|RBR|RBS|VBN|VBG>)*<P>)?)*}
            RelPhrase: {(<RelP1>*|<RelP2>*)?}
    """
    
    def __init__(self, grammer = None):
        self.grammer = grammer or self.RelPhraseGrammer
        self.parser = nltk.RegexpParser(self.grammer)
    
    
    def parse(self, tokenized_sent):
        
        return self.parser.parse(tokenized_sent)
    