import nltk

class RelationGrammerParser(object):
    
    RelPhraseGrammer = r"""
            V: {<RB>?<MD|VB|VBD|VBP|VBG|VBN><RP|RB>?}
            P: {<RB>?<IN|TO|RP><RB>?}
            W: {<PRP$|CD|DT|JJ|JJS|JJR|NN|NNS|NNP|NNPS|POS|RB|RBR|RBS|VBN|VBG>*}
            RelP1: {(<V><P>?)*}
            RelP2: {(<V>(<W>*<P>)?)*}
            RelPhrase: {(<RelP1>*|<RelP2>*)?}
    """
    
    def __init__(self, grammer = None):
        self.grammer = grammer or self.RelPhraseGrammer
        self.parser = nltk.RegexpParser(self.grammer)
    
    
    def parse(self, tokenized_sent):
        
        return self.parser.parse(tokenized_sent)
    