import nltk
import types
from nltk.corpus import conll2000
from nltk.chunk.util import conlltags2tree
from entity_extract.extractor.parsers.base_parser import BaseParser		
    
    

class ChunkParser(nltk.ChunkParserI, BaseParser):

    def __init__(self, chunk_types=['NP'], train_sents=None):
        if not train_sents:
            train_sents = conll2000.chunked_sents('train.txt', chunk_types)
    	train_data = [[(t,c) for w,t,c in nltk.chunk.tree2conlltags(sent)] for sent in train_sents]
    	self.tagger = nltk.TrigramTagger(train_data)
    
    def parse(self, sentence):
    	pos_tags = [pos for (word, pos) in sentence]
    	tagged_pos_tags = self.tagger.tag(pos_tags)
    	
    	return tagged_pos_tags
    	
    	
    def parseBoundaries(self, sentence, phrase_type = []):
        """Method to parse a sentence and return the boundaries of a given 
           tag type - such as relationalPhrases """
        
        if isinstance(phrase_type, types.StringTypes):
            phrase_type = [phrase_type]
            
        parsed_sent = self.parse(sentence)
        chunktags = [chunktag for (pos, chunktag) in parsed_sent]
        
        parseState = {p : None for p in phrase_type}
        bounds = {p:[] for p in phrase_type}
        
        
        def _close_open_phrases(curIndex):
            """ Closes any open phrases in a parseState object """
            for phrase, start in parseState.iteritems():
                if start != None:
                    try:
                        bounds[phrase].append((start, curIndex))
                    except KeyError:
                        bounds[phrase] = [(start, curIndex,)]
                        
                    parseState[phrase] = None
        
        
        for i, cTag in enumerate(chunktags):
            
            if cTag[0] == 'B':
                
                # We're going to begin a tag - so let's store the phrase start point
                if cTag[2:] in parseState and parseState[cTag[2:]] != None:
                    try:
                        bounds[cTag[2:]].append((parseState[cTag[2:]], i,))
                    except KeyError:
                        bounds[cTag[2:]] = [(parseState[cTag[2:]], i,)]
                    
                parseState[cTag[2:]] = i
            
            elif cTag[0] == 'O':
                # We need to close any open tags...
                _close_open_phrases(i)
        
        
        # It's possible tags could still be in the middle - once boundary identification is done
        # So we'll run through the dict of phrases to see if any are still open
        _close_open_phrases(len(chunktags))
        
        return bounds