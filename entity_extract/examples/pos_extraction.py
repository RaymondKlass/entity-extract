
#from entity_extract.extractor.extractors import PosExtractor
from entity_extract.extractor.utilities import SentSplit

p = PosExtractor()
data = p.extract_entities('This is a sentence about the pie in the sky.  If would be interesting.  If only there was')

for d in data:
    print d