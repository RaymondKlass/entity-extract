"""
Base Class for Parsers - ensures that make shift parsers implement the
same standard methods as NLTK parsers.
"""

class BaseParser(object):
    
    def __init__(self):
        pass
    
    def parse(self, sentence):
        """Method to parse a sentence - required to be implemented """
        raise NotImplementedError("Parse method has not been implemented")