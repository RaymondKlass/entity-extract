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
            
    # For the below to work - we'd need the parse Boundaries to populate a class attribute
    def collapseBoundaries(self, bounds, phrase_type):
        """Method to collapse parse bounds - of specific phrases - or all if none are specified """
        #raise NotImplementedError("Collapse Boundaries must be implemented")
        returnBounds = {}
        for phraseType in bounds.keys():
            if not len(phrase_type) or phraseType in phrase_type:
                returnBounds[phrase_type] = self._collapseBounds(bounds, phrase_type)
                
    def _collapseBounds(phrase_type):
        """Recursive method responsible for collapsing bounds """
        
        sortedPhrases = sorted(self.parseBoundaries[phrase_type], key = lambda x : x[0])
        print sortedPhrases
    

""" 
Base Class for Tree based parsers
"""

class BaseTreeParser(BaseParser):
    
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
                tag.label()
                inc = self._count_and_extract(cur_position, tag, boundsByTag, phrase_type)           
            except AttributeError:
                inc = 1
            
            cur_position += inc
        
        return boundsByTag
    
    
    
    def _count_and_extract(self, cur_position, t, boundsByTag, phrase_type):
        """ Recursively discover tags and append their bounds if in phrase_type"""
        try:
            t.label()
            cP = cur_position
            for child in t:
                cP += self._count_and_extract(cP, child, boundsByTag, phrase_type)
                   
            if t.label() in phrase_type or not len(phrase_type):
                try:
                    boundsByTag[t.label()].append( (cur_position, cP,) )
                except KeyError:
                    boundsByTag[t.label()] = [(cur_position, cP,)]
                    
            return cP - cur_position    
        except AttributeError:
            return 1