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
    	
    	
    def parseBoundaries(self, sentence, phrase_type = ['NP']):
        """Method to parse a sentence and return the boundaries of a given 
           tag type - such as relationalPhrases """
        
        if isinstance(phrase_type, types.StringTypes):
            phrase_type = [phrase_type]
            
        parsed_sent = self.parse(sentence)
        chunktags = [chunktag for (pos, chunktag) in parsed_sent]
        
        parseState = {p : False for p in phrase_type}
        bounds = {p:[] for p in phrase_type}
        
        
        def _close_open_phrases():
            """ Closes any open phrases in a parseState object """
            for phrase, start in parseState.iteritems():
                if start:
                    bounds[phrase].append((start, i))
                    parseState[phrase] = False
        
        
        for i, cTag in enumerate(chunktags):
            if cTag[0] == 'B':
                # We're going to begin a tag - so let's store the phrase start point
                if parseState[cTag[2:]]:
                    bounds[cTag[2:]].append((parseState[cTag[2:]], i,))
                    
                parseState[cTag[2:]] = i
            
            elif cTag[0] == 'O':
                # We need to close any open tags...
                _close_open_phrases()
        
        
        # It's possible tags could still be in the middle - once boundary identification is done
        # So we'll run through the dict of phrases to see if any are still open
        _close_open_phrases()
        
        return bounds