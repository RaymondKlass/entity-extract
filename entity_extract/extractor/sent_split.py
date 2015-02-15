# Split Sentences 

import nltk

class SentSplit(object):
    
    def __init__(self):
        self.sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    
    def split(self, raw_corpus):
        return self.sent_tokenizer.tokenize(raw_corpus)