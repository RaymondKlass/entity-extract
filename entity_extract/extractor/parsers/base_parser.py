"""
Base Class for Parsers - ensures that make shift parsers implement the
same standard methods as NLTK parsers.
"""

class BaseParser(object):
    
    def __init__(self):
        pass
    
    def parse(self, sentence):
        """Method to parse a sentence - required to be implemented """
        raise NotImplementedError("Parse method has not been implemented")
        
    def parseBoundaries(self, sentence):
        """Method to parse a sentence and return the boundaries of a given 
           tag type - such as relationalPhrases """
    
        parsed_sent = self.parse(sentence)
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