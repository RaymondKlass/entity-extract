
#from entity_extract.extractor.extractors import PosExtractor
from entity_extract.extractor.utilities import SentSplit, Tokenizer
from entity_extract.extractor.pos_tagger import PosTagger
from entity_extract.extractor.parsers import ChunkParser, RelationGrammerParser
from entity_extract.extractor.extractors.pos_extractor import PosRelationExtractor

# Initialize Services
sentSplitter = SentSplit()
tokenizer = Tokenizer()
tagger = PosTagger()
chunker = ChunkParser()
grammerParse = RelationGrammerParser()
posExtractor = PosRelationExtractor()



sents = sentSplitter.split('The big orange tiger ran across the green grass field.  Sean White won the Olympic Gold metal in snowboarding.')
for sent in sents:
    tokens = tokenizer.tokenize(sent)
    tags = tagger.tag(tokens)

    npChunks = chunker.collapseBoundaries( chunker.parseBoundaries(tags, ['NP']) )

    relParse = grammerParse.collapseBoundaries( grammerParse.parseBoundaries(tags, ['RelPhrase']) )

    extract = posExtractor.extract(tokens, npChunks['NP'], relParse['RelPhrase'])
    
    print extract
    
    
