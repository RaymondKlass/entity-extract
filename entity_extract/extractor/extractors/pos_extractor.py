import nltk

class PosRelationExtractor(object):

    def __init__(self, debug = False):
        pass
        
    
    def extract(self, token_sent, np_bounds, rel_bounds):
        """ Extract relationships based upon entity's found in Noun Phrases and 
            Relational Phrases - A simple approach - if we find Relational Phrases
            that are surrounded by Noun Phrases, then we'll call this a relationship
        """
        
        all_bounds = [(b[0], b[1], 'NP', token_sent[b[0]:b[1]]) for b in np_bounds]
        all_bounds += [(b[0], b[1], 'REL', token_sent[b[0]: b[1]]) for b in rel_bounds]
        
        all_bounds = sorted(all_bounds, key = lambda x: x[0])
        
        # Will the bounds sorted together - we're going to look for NP -> REL -> NP
        # Since we've already collapsed boundaries, there is no need to worry about overlap
        
        relations = []
        temp_rel = []
        
        for phrase in all_bounds:
            if phrase[2] == 'NP':
                # This phrase could either be a start or an end - or both
                try:
                    if temp_rel[-1][2] == 'REL':
                        temp_rel[-1].append(phrase)
                        relations.append(phrase)
                        temp_rel = [phrase]
                    
                    elif temp_rel[-1][2] == 'NP':
                        temp_rel[-1] = phrase
                
                except KeyError:
                    temp_rel = [phrase]
            
            elif phrase[2] == 'REL':
                try:
                    if temp_rel[-1][2] == 'NP':
                        temp_rel.append(phrase)
                    elif temp_rel[-1][2] == 'REL':
                        # Two in a row is not valid, so we should reset the temp var
                        temp_rel = []
                except KeyError:
                    # Only occurs if this is the first phrase trying to be pushed on - which is not valid
                    pass
        
        return relations