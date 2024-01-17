import logging
import os
from datetime import datetime

# we use f-string when we use variable in string 
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)

os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

# if I want to extend functionalities of logging ,I have to do it in logging.basicConfig
logging.basicConfig(
  filename=LOG_FILE_PATH,
  format="[ %(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
  level=logging.INFO
)

if __name__=="__main__":
    logging.info('Logging has started')


