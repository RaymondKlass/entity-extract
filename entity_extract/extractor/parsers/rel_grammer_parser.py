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
    
    
    # We should better generalize this tree bounds extraction as a utility function
    
    
    def parse(self, tokenized_sent):
        
        parsed_sent = self.parser.parse(tokenized_sent)
        
        # since we've got to unfold potentially compound phrases - 
        # we can't rely on enumeration - so we need our own counter
        cur_position = 0
        bounds = []
        
    
        for i, tag in enumerate(parsed_sent):
            try:
                # Prints the label of the node ( - for this case - RelPhrase )
                # print tag.node
                tag.node
                inc = self._count_leaves(tag)
                bounds.append((cur_position, cur_position + inc,))
            except AttributeError:
                inc = 1
            
            cur_position += inc
        
        return bounds
    
    def _count_leaves(self, t):
        try:
            t.node
            return sum([self._count_leaves(child) for child in t])
        except AttributeError:
            return 1
            
    
    
    