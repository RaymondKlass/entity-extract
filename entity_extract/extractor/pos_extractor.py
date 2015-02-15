# Part of Speach (POS) Based Entity Extraction
# Aimed at Extracting Relationships
from .sent_split import SentSplit

class PosExtractor(object):

    def __init__(self, debug = False):
        self.sentSplit = SentSplit()