
from extractor import PosExtractor

p = PosExtractor()
split = p.sentSplit.split('This is a sentence about the pie in the sky.  If would be interesting.  If only there was')
print(split)
tokens = (p.tokenizer.tokenize(s) for s in split)
print tokens
pos = (p.pos_tagger.tag(t) for t in tokens)
print pos
for data in pos:
    print data