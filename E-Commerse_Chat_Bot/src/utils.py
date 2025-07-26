import os 
import dill

import sys 
from src.exception.exception import ProjectException


import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

import re

nltk.download("wordnet")
nltk.download("stopwords")
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('wordnet')

def part_of_speach(token):
    pos_tags =  nltk.pos_tag([token])
    pos_tag = pos_tags[0][1]

    if pos_tag.startswith('J'):
        return wordnet.ADJ
    elif pos_tag.startswith('V'):
        return wordnet.VERB
    elif pos_tag.startswith('N'):
        return wordnet.NOUN
    elif pos_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN
    
    
    
def apply_preprocessing(text):
    try:
        lemmatizer = WordNetLemmatizer()
        stop_words = set(stopwords.words("english"))
        
        text = text.lower()
        text = re.sub(r'[^\w\s]','',text)
        tokens = word_tokenize(text)
        filtered_tokens = [token for token in tokens if token not in stop_words]

        lemmatized_tokens = [lemmatizer.lemmatize(token ,part_of_speach(token)) for token in filtered_tokens]
        preprocessed_text = ' '.join(lemmatized_tokens)
    
        return preprocessed_text
    
    except Exception as e:
        raise ProjectException(e ,sys)
    
                

def save_object(file_path ,obj):
    try:
        with open(file_path, 'wb') as f:
            dill.dump(obj, f)
    
    except Exception as e:
        raise ProjectException(e,sys)
    
    
def load_object(file_path):
    try:
        with open(file_path, 'rb') as f:
            return dill.load(f)
    
    except Exception as e:
        raise ProjectException(e,sys)


def evaluate_model(X_train , Y_train , X_test , Y_test , models):
    report={}
    for i in range(len(list(models))):
        
        model = list(models.values())[i]
        model.fit(X_train,Y_train)
        test_score =  model.score(X_test,Y_test)
        train_score = model.score(X_train,Y_train)
        report[ list(models.values())[i]] = test_score
    
    return report