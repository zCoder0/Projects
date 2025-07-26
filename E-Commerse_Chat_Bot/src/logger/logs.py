import logging
from datetime import datetime as dt
import os


file_name= f"{dt.now().strftime('%m_%d_%Y_%H')}.log"

log_file =os.path.join(os.getcwd(),"logs",file_name)

os.makedirs(log_file,exist_ok=True)


log_file_path = os.path.join(log_file,file_name)


logging.basicConfig(
    level=logging.INFO,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    filename=log_file_path,
)