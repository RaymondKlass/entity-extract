# Part of Speach (POS) Based Entity Extraction
# Aimed at Extracting Relationships
from .sent_split import SentSplit
from .tokenizer import Tokenizer
from .pos_tagger import PosTagger

class PosExtractor(object):

    def __init__(self, debug = False):
        self.sentSplit = SentSplit()
        self.tokenizer = Tokenizer()
        self.pos_tagger = PosTagger()