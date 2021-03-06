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
    def collapseBoundaries(self, bounds, phrase_type = []):
        """ Method to collapse parse bounds - of specific phrases - or all if none are specified 
            Returns collapsed bounds along with un-collapsed bounds if phrases exists that were not 
            specified for collapse 
        """
        
        returnBounds = {}
        for phraseType in bounds.keys():
            if not len(phrase_type) or phraseType in phrase_type:
                returnBounds[phraseType] = self._collapseBounds(bounds[phraseType])
            else:
                returnBounds[phraseType] = bounds[phraseType]
        
        return returnBounds
                
    def _collapseBounds(self, bounds):
        """Perform the bounds collapse - and return a new list, fully collapsed"""
        sortedPhrases = sorted(bounds, key = lambda x : x[0])

        collapsedBounds = []
        for boundPair in sortedPhrases:
            try:
                if boundPair[0] <= collapsedBounds[-1][1]:
                    if boundPair[1] > collapsedBounds[-1][1]:
                        collapsedBounds[-1] = (collapsedBounds[-1][0], boundPair[1],)
                else:
                    collapsedBounds.append(boundPair)

            except IndexError:
                # Throws an index error for the first boundPair - as collpasedBounds[-1] doesn't exist
                collapsedBounds.append(boundPair)
        
        return collapsedBounds
                
    

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