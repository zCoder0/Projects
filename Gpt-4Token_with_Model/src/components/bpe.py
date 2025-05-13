import sys
from src.exception.custom_exception import ProjectException
from collections import defaultdict
class BPE:
    
    def __init__(self):
        pass
    
    def get_stats(self,ids):
        try:
            stats = defaultdict(int)
            for seq in ids:
                for i in range(len(seq) - 1):
                    pair = (seq[i], seq[i+1])
                    stats[pair] += 1
                    
            return stats
    
        except Exception as e:
            print("Error ",e)
            ProjectException(e,sys)
        

    def merge_ids(self,ids, pair, new_id):
        """ Merge a given byte pair across all token byte sequences """
        new_ids = []
        for seq in ids:
            i = 0
            merged = []
            while i < len(seq):
                if i < len(seq)-1 and (seq[i], seq[i+1]) == pair:
                    merged.append(new_id)
                    i += 2
                else:
                    merged.append(seq[i])
                    i += 1
            new_ids.append(merged)
        return new_ids
    
    
    
    """    monday 
    
    sunday 18 -m 4-4
    
    """