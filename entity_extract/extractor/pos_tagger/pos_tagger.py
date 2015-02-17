# Part of Speach Tagger

import nltk

class PosTagger(object):
    
    def __init__(self):
        self.pos_tagger = nltk.pos_tag
    
    def tag(self, sent_tokenized):
        return self.pos_tagger(sent_tokenized)