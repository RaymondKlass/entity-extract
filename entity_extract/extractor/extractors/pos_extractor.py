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

class PosExtractor(object):

    def __init__(self, debug = False):
        pass
        
    # Generator to return tokenized sentences
    def extract_entities(self, token_sent):
        grammer = r"""
            V: {<RB>?<MD|VB|VBD|VBP|VBG|VBN><RP|RB>?}
            P: {<RB>?<IN|TO|RP><RB>?}
            W: {<PRP$|CD|DT|JJ|JJS|JJR|NN|NNS|NNP|NNPS|POS|RB|RBR|RBS|VBN|VBG>*}
        """
        
        cp = nltk.RegexpParser(grammer)
        
        return cp.parse(token_sent)

