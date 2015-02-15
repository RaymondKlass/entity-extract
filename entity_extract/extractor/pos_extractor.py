# Part of Speach (POS) Based Entity Extraction
# Aimed at Extracting Relationships
from .sent_split import SentSplit
from .tokenizer import Tokenizer
from .pos_tagger import PosTagger

class PosExtractor(object):

    def __init__(self, debug = False):
        
        # These will liekly be run as separate services - but for 
        # development ease I'm including them here for the time being.
        
        self.sentSplit = SentSplit()
        self.tokenizer = Tokenizer()
        self.pos_tagger = PosTagger()
        
    
    def extract_entities(self, raw_corpus):
        
        sents = self.sentSplit.split(raw_corpus)
        for sent in sents:
            tokens = self.tokenizer.tokenize(sent)
            yield self.pos_tagger.tag(tokens)
        