
#from entity_extract.extractor.extractors import PosExtractor
from entity_extract.extractor.utilities import SentSplit, Tokenizer
from entity_extract.extractor.extractors import PosExtractor
from entity_extract.extractor.pos_tagger import PosTagger

#p = PosExtractor()
sents = p.SentPlit('This is a sentence about the pie in the sky.  If would be interesting.  If only there was')
for sent in sents:
    tokens = Tokenizer.tokenize(sent)
    tags = PosTagger(tokens)
    print tags
