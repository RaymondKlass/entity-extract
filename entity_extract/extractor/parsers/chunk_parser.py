import nltk
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
    
    	chunktags = [chunktag for (pos, chunktag) in tagged_pos_tags]
    	
    	relBounds = []
    	
    	start = -1
    	for i, ctag in enumerate(chunktags):
    		if ctag == 'B-NP':
    			start = i
    		if start != -1 and ctag != 'I-NP' and start != i:
    			relBounds.append([start, i-1])
    			start = -1
    	
    	if start != -1:
    		relBounds.append([start, len(chunktags)-1]) # if the last phrase in a NP - append it
    	
    	return relBounds