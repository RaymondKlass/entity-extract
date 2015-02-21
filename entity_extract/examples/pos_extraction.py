
#from entity_extract.extractor.extractors import PosExtractor
from entity_extract.extractor.utilities import SentSplit, Tokenizer
from entity_extract.extractor.extractors import PosExtractor
from entity_extract.extractor.pos_tagger import PosTagger

# Initialize Services
sentSplitter = SentSplit()
tokenizer = Tokenizer()
tagger = PosTagger()


sents = sentSplitter.split('This is a sentence about the pie in the sky.  If would be interesting.  If only there was')
for sent in sents:
    tokens = tokenizer.tokenize(sent)
    tags = tagger.tag(tokens)
    print tags
