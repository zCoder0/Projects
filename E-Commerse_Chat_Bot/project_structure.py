import os
from pathlib import Path

dir = "src"

file_path = [
    f"{dir}\\components\\__init__.py",
    f"{dir}\\components\\data_ingestion.py",
    f"{dir}\\components\\data_preprocess.py",
    f"{dir}\\components\\data_transformation.py",
    f"{dir}\\components\\model_training.py",
    f"{dir}\\components\\data_set\\__init__.py",
    
    f"{dir}\\pipeline\\predicting_pipeline.py",
    
    
    f"{dir}\\exception\\exception.py",
    f"{dir}\\logger\\logs.py",
    f"{dir}\\utils.py",
]


for path in file_path:
    
    files =  Path(path)
    
    folder,file  = os.path.split(files)
    
    if folder != "":
        os.makedirs(folder,exist_ok=True)
        
    
    if (not os.path.exists(files) or os.path.getsize(files)==0 ):
     
        with open(files,"w") as f:
            pass
        
