# Tokenize Split Sentences

import nltk

class Tokenizer(object):
    
    def __init__(self):
        self.tokenizer = nltk.word_tokenize
    
    def tokenize(self, sentence):
        return self.tokenizer(sentence)