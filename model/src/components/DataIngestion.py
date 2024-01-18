import pandas as pd
import os
from dataclasses import dataclass
import sys
from sklearn.model_selection import train_test_split
from src.logger import logging
from src.exception import CustomException
@dataclass
class DataIngestionConfig:

    train_data_path:str=os.path.join("artifacts","train.csv")
    test_data_path:str=os.path.join("artifacts","test.csv")
    raw_data_path:str=os.path.join("artifacts","raw.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion component")
        try:
            # here we can implement logic of reading data from database
            df=pd.read_csv("../../jupyter/Sleep_health_and_lifestyle_dataset.csv")
            # making directory to store files
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)  
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            # reading training and test data
            logging.info("Train-Test split started")
            train_data,test_data=train_test_split(df,test_size=0.2,random_state=42)
            train_data.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_data.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Ingestion of data is completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
         
        except Exception as e:
            CustomException(e,sys)

if __name__=="__main__":
    dataIngestion=DataIngestion()
    dataIngestion.initiate_data_ingestion()
    


    

