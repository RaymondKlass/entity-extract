import nltk
from nltk.corpus import conll2000
from nltk.chunk.util import conlltags2tree


class ChunkParser(object):
    
    def __init__(self, chunk_types=['NP']):
        train_sents = conll2000.chunked_sents('train.txt', chunk_types)
		self.ChunkParser = nltk.ChunkParser(train_sents)
    
    def parse(self, tagged_sent):
        return self.ChunkParser.parse(tagged_sent)		