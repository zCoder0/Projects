from src.exception.exception import ProjectException

import sys

from src.pipeline.predicting_pipeline import PredictingPipeline

if __name__ == "__main__":
    try:
        
        predict = PredictingPipeline()
        
        #text = input("Ask : ")
        text = "I'm wnt to track my order {{Order Number}}"
        
        print(f"Question : {text}")
        res = predict.initiate_predict_model(text)
        
        print(f"\nResponse : {res}")
        

    except Exception as e:
        raise ProjectException(e, sys)
    
    