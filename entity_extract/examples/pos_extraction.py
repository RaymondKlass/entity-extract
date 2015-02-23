
#from entity_extract.extractor.extractors import PosExtractor
from entity_extract.extractor.utilities import SentSplit, Tokenizer
from entity_extract.extractor.extractors import PosExtractor
from entity_extract.extractor.pos_tagger import PosTagger
from entity_extract.extractor.parsers import ChunkParser

# Initialize Services
sentSplitter = SentSplit()
tokenizer = Tokenizer()
tagger = PosTagger()
chunker = ChunkParser()
extractor = PosExtractor()


sents = sentSplitter.split('This is a sentence about the pie in the sky.  If would be interesting.  If only there was')
for sent in sents:
    tokens = tokenizer.tokenize(sent)
    tags = tagger.tag(tokens)
    chunks = chunker.parse(tags)
    print chunks
    print extractor.extract_entities(tags)
