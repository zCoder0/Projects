from transformers import BertTokenizer, BertForSequenceClassification
from src.exception.custom_exception import ProjectException
import torch
import sys
import warnings
warnings.filterwarnings('ignore')

class Model:
    
    def __init__(self , model_name="fzn0x/bert-spam-classification-model"):
    
        self.model_name=model_name
        self.tokenizer=None
        self.model=None
        self.device =None
    
    def load_model(self):
        try:
            self.model = BertForSequenceClassification.from_pretrained(self.model_name, num_labels=2)
            self.tokenizer = BertTokenizer.from_pretrained(self.model_name)
            torch.device("cuda" if torch.cuda.is_available() else "cpu")
            self.model.to(self.device)
            self.model.eval()
        except Exception as e:
            print(f"Error loading model: {e}")
            ProjectException(e,sys)

    def predict(self, text):
        try:
            inputs = self.tokenizer(text, return_tensors="pt", truncation=True, padding=True).to(self.device)
            with torch.no_grad():
                outputs = self.model(**inputs)
            logits = outputs.logits
            prediction = torch.argmax(logits, dim=1).item()
            return 'SPAM' if prediction == 1 else 'HAM'
        except Exception as e:
            print(f"Error making prediction: {e}")
            ProjectException(e,sys)
            
            
    def save_model(self):
        try:
            if self.model is not None:
                self.model.save_pretrained(self.model_name)
                self.tokenizer.save_pretrained(self.model_name)

        except Exception as e:
            print(f"Error saving model: {e}")
            ProjectException(e,sys)
            