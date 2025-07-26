
import os 

from dataclasses import dataclass

import pandas as pd

from sklearn.model_selection import train_test_split

from src.exception.exception import ProjectException
from src.logger.logs import logging

import sys


from src.components.data_ingestion import DataIngestion
from src.components.data_preprocess import DataPreprocessing
from src.components.data_transformation import DataTransformation
from src.components.model_training import ModelTraining



@dataclass
class DataIngestionConfigure:
    train_data_path:str = os.path.join("artifacts","train.csv")
    test_data_path:str= os.path.join("artifacts","test.csv")
    raw_data_path :str = os.path.join("artifacts","raw.csv")
        
class DataIngestion:
    
    def __init__(self):
        
        self.ingestion_config = DataIngestionConfigure()
        
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method")
        
        try:
            df= pd.read_csv("src/components/data_set/Customer_data.csv")
            
            logging.info("DataSet readed Successfully")
            
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path) ,exist_ok=True)
            
            X_train , X_test = train_test_split(df , test_size=0.2 ,random_state=42)
           
            
            df.to_csv(self.ingestion_config.raw_data_path ,index=False , header=True)
            X_train.to_csv(self.ingestion_config.train_data_path,index=False ,header=True)
            X_test.to_csv(self.ingestion_config.test_data_path,index=False ,header=True)
            
            
            logging.info("X_Train and X_test created successfully\n")   
             
            
            return(
               self.ingestion_config.train_data_path,
               self.ingestion_config.test_data_path,
            )

        except Exception as e:
            raise ProjectException(e, sys) 


if __name__ == "__main__":
    
    try:
        
        data_ingestion = DataIngestion()
        X_train_path,X_test_path = data_ingestion.initiate_data_ingestion()
        
        data_preprocessing = DataPreprocessing()
        X_train_preprocess_path , X_test_preprocess_path =  data_preprocessing .initiate_data_preprocessing(X_train_path,X_test_path)
        
        
        data_transform = DataTransformation()
        train_arr , test_arr = data_transform.initiate_transform_data( X_train_preprocess_path ,X_test_preprocess_path)

        model_training = ModelTraining()
        model_training.initiate_model_training(train_arr,test_arr)
    
    except Exception as e:
        raise ProjectException(e, sys)
