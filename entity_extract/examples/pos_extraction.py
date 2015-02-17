
from entity_extract.extractor import PosExtractor

p = PosExtractor()
data = p.extract_entities('This is a sentence about the pie in the sky.  If would be interesting.  If only there was')

for d in data:
    print d