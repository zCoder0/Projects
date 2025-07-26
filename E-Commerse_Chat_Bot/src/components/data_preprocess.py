import os 
import pandas  as pd
import numpy 

from src.exception.exception import ProjectException
from src.logger.logs import logging

from src.utils import apply_preprocessing

from dataclasses import dataclass

@dataclass
class DataPreprcoessingConfigure:
    """Data Preprocessing Configuration Class"""
    
    preprocess_train_path = os.path.join("artifacts","train_preprocess.csv")
    preprocess_test_path = os.path.join("artifacts","test_preprocess.csv")
    
    preprocess_path = os.path.join("artifacts","preprocess.pkl")
    
    
class DataPreprocessing:
    
    def __init__(self):
        self.preprocessing_config = DataPreprcoessingConfigure()

    
    def initiate_data_preprocessing(self ,X_train_path,X_test_path):
        """Initiate Data Preprocessing"""
    
        logging.info("Entered Preprocessing Method")
        
        
        X_train = pd.read_csv(X_train_path)
        X_test = pd.read_csv(X_test_path)
        
        X_train['preprocessed_instruction'] =X_train['instruction'].apply(apply_preprocessing)
        X_test['preprocessed_instruction'] =X_test['instruction'].apply(apply_preprocessing)

        logging.info("Preprocess Done")
        
        X_train.to_csv(self.preprocessing_config.preprocess_train_path)
        X_test.to_csv(self.preprocessing_config.preprocess_test_path)
        
        logging.info("Saved Sucessfully \n")
        
        return(
            self.preprocessing_config.preprocess_train_path ,
            self.preprocessing_config.preprocess_test_path
        )


        
    