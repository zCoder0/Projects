import os 

from src.exception.exception import ProjectException
from src.logger.logs import logging

from dataclasses import dataclass 

import pandas as pd

from src.utils import load_object , apply_preprocessing

import sys
import numpy as np

@dataclass
class PredictingPipelineConfig:
    model_path = os.path.join("artifacts", "model.pkl")
    tfidf_pipe_path = os.path.join("artifacts","tfidf_pipline.pkl")
    label_pipe_path = os.path.join("artifacts","label_pipeline.pkl")
    raw_data_path= os.path.join("artifacts","raw.csv")

class PredictingPipeline:
    
    def __init__(self):
        self.predicting_config = PredictingPipelineConfig()
        
        self.raw_df = pd.read_csv(self.predicting_config.raw_data_path)
        self.le = load_object(self.predicting_config.label_pipe_path)
        
    def __predict_response(self , intent):
        try:
            logging.info("Entered response method ")
            intent =  self.le.classes_[intent]
            rand = np.random.randint(0,100)
            response = self.raw_df[self.raw_df['intent']==intent]['response'].values[rand]
            
            return response
            
        except Exception as e:
            raise ProjectException(e ,sys)
            
            
    def initiate_predict_model(self, text):
        
        try:
            logging.info("Enterd into initiate predict model")
            preprocessed_text =  apply_preprocessing(text)
            
            tfidf_pipe = load_object(self.predicting_config.tfidf_pipe_path)
            
            vector  = tfidf_pipe.transform([preprocessed_text])
            
            
            logging.info("Predicting...")
            
            model = load_object(self.predicting_config.model_path)
        
            OUTPUT = model.predict(vector)

            RES = self.__predict_response(OUTPUT[0])

            logging.info("Respose are : " + str(RES))
            
            return RES

            
        except Exception as e: 
            raise ProjectException(e,sys)
        