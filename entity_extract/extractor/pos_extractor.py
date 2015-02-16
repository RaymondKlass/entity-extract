# Part of Speach (POS) Based Entity Extraction
# Aimed at Extracting Relationships
from .sent_split import SentSplit
from .tokenizer import Tokenizer
from .pos_tagger import PosTagger

class PosExtractor(object):

    def __init__(self, debug = False):
        
        # These will liekly be run as separate services - but for 
        # development ease I'm including them here for the time being.
        
        self._sentSplit = SentSplit()
        self._tokenizer = Tokenizer()
        self._pos_tagger = PosTagger()
        
    # Generator to return tokenized sentences
    def extract_entities(self, raw_corpus):
        
        sents = self._sentSplit.split(raw_corpus)
        for sent in sents:
            tokens = self._tokenizer.tokenize(sent)
            tags = self._pos_tagger.tag(tokens)

            yield tags
        