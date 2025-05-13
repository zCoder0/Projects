
import sys
from src.exception.custom_exception import ProjectException


class Prerprocessing:
    def __init__(self):
        pass
    
    def chat_format(self,data):
        try:
            user = data.get('text', '')
            assistant = data.get('response', '')
            return f"<|im_start|>user<|im_sep|>{user}<|im_end|><|im_start|>assistant<|im_sep|>{assistant}<|im_end|><EOS>"
        except Exception as e:
            print("Error ",e)
            ProjectException(e,sys)

