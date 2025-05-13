from src.components.bpe import BPE
import sys
from src.exception.custom_exception import ProjectException
import regex as re 

class Tokenizer:
    
    def __init__(self,max_length=100):
        self.bpe = BPE()
        self.GPT4_SPLIT_PATTERN = r"""'(?i:[sdmt]|ll|ve|re)|[^\r\n\p{L}\p{N}]?+\p{L}+|\p{N}{1,3}| ?[^\s\p{L}\p{N}]++[\r\n]*|\s*[\r\n]|\s+(?!\S)|\s+"""
        self.merges={}
        self.ids={}
        self.original_len=0
        self.max_length = max_length
        self.special_tokens = {'<PAD>':10000, '<EOS>': 10001}
        
    def encoder(self,sentence,num_merges=1000):
        try:
            tokens = re.findall(self.GPT4_SPLIT_PATTERN, sentence)
            self.ids = [list(token.encode("utf-8")) for token in tokens]
            self.merges = {}
            for i in range(num_merges):
                stats = self.bpe.get_stats(self.ids)
                if not stats:
                    break
                pair = max(stats, key=stats.get)
                new_id = 256 + i
                self.ids = self.bpe.merge_ids(self.ids, pair, new_id)
                self.merges[pair] = new_id
                print(f"Merge {pair} -> {new_id}")

            # Step 4: Flatten final ids
            flattened_ids = [item for sublist in self.ids for item in sublist]
            return flattened_ids, self.merges
  
        except Exception as e:
            print("Error ",e)
            ProjectException(e,sys)
    
    def get_vocab(self,merges=None):
        if merges == None:
            merges = self.merges

        vocab ={idx: bytes([idx]) for idx in range(256)}
        for (p0,p1),idx in merges.items():
            vocab[idx] = vocab[p0] + vocab[p1]

        return vocab
    
    
    def decode(self,ids,merges=None):
        try:
            if self.merges == {}:
                return None
            if merges == None:
                merges = self.merges

            vocab = self.get_vocab(merges)
            text =""
            for id in ids:
                if id == self.special_tokens['<EOS>']:
                    break
                if id == self.special_tokens['<PAD>']:
                    continue
                text += vocab[id].decode("utf-8", errors="replace")

            return text
        except Exception as e:
            print("Error ",e)
            ProjectException(e,sys)
            
    
    