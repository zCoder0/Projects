import os 

from src.exception.exception import ProjectException
from src.logger.logs import logging

import sys 

import pandas 
import numpy as np 

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

from dataclasses import dataclass
from src.utils import save_object
import pandas as pd

@dataclass
class DataTransformationConfigure:
    """DataTransformationConfigure class."""
    tfidf_transformation_path = os.path.join("artifacts","tfidf_pipline.pkl")
    label_transformation_path =os.path.join("artifacts","label_pipeline.pkl")

class DataTransformation:
    
    def __init__(self):
        self.data_transformer_configure = DataTransformationConfigure()
        
    def get_data_transformer_object(self):
        
        try:
            
            logging.info("Entered transformer_object method")
            
            column_names = ['flags', 'instruction', 'category', 'intent', 'response']
            
            
            vectorizer = TfidfVectorizer(max_features=500)
            
            label_encoder = LabelEncoder()
            
    
            logging.info("successfully created transformer objects\n")
            
            return vectorizer, label_encoder
        
        except Exception as e:
            raise ProjectException(e,sys)   
        
        
    def initiate_transform_data(self ,x_train_path ,x_test_path):
        try:
            
            logging.info("Entered initiate_transform_data method")
            
            train_df = pd.read_csv(x_train_path)
            test_df = pd.read_csv(x_test_path)
            
            logging.info("dataset successfully readed")
            
            tfidf_tansformer_pipeline ,  label_transformer_pipeline = self.get_data_transformer_object()
            
            print(tfidf_tansformer_pipeline)
            print()
            
            input_feature_train_df = train_df['instruction']
            target_feature_train_df = train_df['intent']
            
            input_feature_test_df = test_df['instruction']
            target_feature_test_df = test_df['intent']
    
            
            input_feature_train_df = (input_feature_train_df.values).ravel()
            input_feature_test_df = (input_feature_test_df.values).ravel()
            
            print("Input Feature value\n")
            print(input_feature_train_df)
            
            print("\nTarget Feature Value\n")
            print(target_feature_test_df)
            
            
            target_feature_train_df = label_transformer_pipeline.fit_transform(target_feature_train_df)
            target_feature_test_df = label_transformer_pipeline.transform(target_feature_test_df)
            
            input_feature_train_df =  tfidf_tansformer_pipeline.fit_transform(input_feature_train_df)
            input_feature_test_df =  tfidf_tansformer_pipeline.transform(input_feature_test_df)
            
            
            logging.info("Applied transformer on data")
            
            #create a array
            
            train_arr =( input_feature_train_df , target_feature_train_df )
            
            test_arr =( input_feature_test_df,target_feature_test_df)
        
           
            
            logging.info("converted array")
            
            save_object(file_path =self.data_transformer_configure.tfidf_transformation_path,
                        obj = tfidf_tansformer_pipeline)
            save_object(file_path = self.data_transformer_configure.label_transformation_path , 
                        obj = label_transformer_pipeline)
            
            
            logging.info("Piplines are saved\n")
            
            return (
                train_arr ,
                test_arr
            )
            
        except Exception as e:
            raise ProjectException(e,sys)