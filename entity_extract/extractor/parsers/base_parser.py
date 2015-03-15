import types

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
    
    
    # Needs to be updated to honor specific phrase types
    def parseBoundaries(self, sentence, phrase_type = []):
        """Method to parse a sentence and return the boundaries of a given 
           tag type - such as relationalPhrases """
        raise NotImplementedError("Parse Boundary method has not been implemented")
            


""" 
Base Class for Tree based parsers
"""

class BaseTreeParser(object):
    
    def __init__(self):
        pass
    
    
    def parseBoundaries(self, sentence, phrase_type = []):
        """Method to parse a sentence and return the boundaries of a given 
           tag type - such as relationalPhrases """
        
        if isinstance(phrase_type, types.StringTypes):
            phrase_type = [phrase_type]
        
        parsed_sent = self.parse(sentence)
        cur_position = 0
        boundsByTag = {p:[] for p in phrase_type}
        
        for i, tag in enumerate(parsed_sent):
            try:
                tag.node
                inc = self._count_and_extract(cur_position, tag, boundsByTag, phrase_type)           
            except AttributeError:
                inc = 1
            
            cur_position += inc

        return boundsByTag
    
    
    
    def _count_and_extract(self, cur_position, t, boundsByTag, phrase_type):
        """ Recursively discover tags and append their bounds if in phrase_type"""
        try:
            t.node
            cP = cur_position
            for child in t:
                cP += self._count_and_extract(cP, child, boundsByTag, phrase_type)
                   
            if t.node in phrase_type:
                boundsByTag[t.node].append( (cur_position, cP,) )
                
            return cP - cur_position    
        except AttributeError:
            return 1