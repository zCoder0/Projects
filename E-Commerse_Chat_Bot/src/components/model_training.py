import os 
from src.exception.exception import ProjectException
from src.logger.logs import logging
import sys 

from sklearn.naive_bayes import MultinomialNB

from dataclasses import dataclass 
from src.utils import evaluate_model ,save_object
@dataclass 
class ModelTrainingConfigure:
    model_path:str = os.path.join("artifacts","model.pkl")


class ModelTraining:
    
    def __init__(self):
        self.model_training_configure = ModelTrainingConfigure()

    
    def initiate_model_training(self ,train_arr ,test_arr):
        

        logging.info("Entered into Model Training")
        try:
            
            logging.info("Split train and test data ")

            X_train,Y_train  ,X_test ,Y_test =(
                train_arr[0],
                train_arr[1],
                
                test_arr[0],
                test_arr[1]
            )
            
            models ={
                "Multinomial":MultinomialNB(),
            }
            
            logging.info("Model created ")
            report:dict = evaluate_model( 
                
                X_train =X_train , Y_train =Y_train , X_test =X_test , Y_test =Y_test ,models = models
            
            )

            
            best_score =  max(report.values())         
               
            best_model_name = list(models.keys())[list(report.values()).index(best_score)]
   
            best_model = models[best_model_name]
            
            if best_score <0.6:
                logging.info("Model is not good enough , need to tune the hyperparameters")
                return None
            
            save_object(
                file_path= self.model_training_configure.model_path,
                obj=best_model
            )
            
            logging.info("Model Saved Sucessfully")

            
        except Exception as e:
            raise ProjectException(e,sys)