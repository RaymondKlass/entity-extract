
#from entity_extract.extractor.extractors import PosExtractor
from entity_extract.extractor.utilities import SentSplit, Tokenizer
from entity_extract.extractor.pos_tagger import PosTagger
from entity_extract.extractor.parsers import ChunkParser, RelationGrammerParser

# Initialize Services
sentSplitter = SentSplit()
tokenizer = Tokenizer()
tagger = PosTagger()
chunker = ChunkParser()
grammerParse = RelationGrammerParser()



sents = sentSplitter.split('The big orange tiger ran across the green grass field.  Sean White won the Olympic Gold metal in snowboarding.')
for sent in sents:
    tokens = tokenizer.tokenize(sent)
    tags = tagger.tag(tokens)
    chunks = chunker.parse(tags)
    print chunker.parseBoundaries(tags)
    print chunks
    #print grammerParse.parse(tags)
    #print grammerParse.parseBoundaries(tags, ['RelPhrase'])
