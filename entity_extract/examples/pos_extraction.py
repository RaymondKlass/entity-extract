
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

while True:
    print 'Enter a Sentence, or press X to exit'
    sent = raw_input()
    
    if sent == 'X':
        print 'Exiting...'
        break
    
    print '\n'
    print '-------------------------'
    print '\n'
    
    tokens = tokenizer.tokenize(sent)
    tags = tagger.tag(tokens)

    npChunks = chunker.collapseBoundaries( chunker.parseBoundaries(tags, ['NP']) )

    relParse = grammerParse.collapseBoundaries( grammerParse.parseBoundaries(tags, ['RelPhrase']) )

    extract = posExtractor.extract(tokens, npChunks['NP'], relParse['RelPhrase'])
    
    for relation in extract:
        print ' '.join(relation[0][3]) + ' -> ' + ' '.join(relation[1][3]) + ' -> ' + ' '.join(relation[2][3])
    
    if not len(extract):
        print 'No Relationships Found'