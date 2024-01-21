import sys
from src.exception import CustomException
import os
from src.utils import load_object
import pandas as pd

class PredictPipeline:
    def __init__(self):
        pass
    def predict(self,features):

        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join("artifacts","preprocessor.pkl")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            features[['Systolic_blood_pressure','Diastolic_blood_pressure']]=features['Blood_Pressure'].str.split('/',expand=True)
            features=features.drop('Blood_Pressure',axis=1)
            features['Systolic_blood_pressure']=features['Systolic_blood_pressure'].astype('int')
            features['Diastolic_blood_pressure']=features['Diastolic_blood_pressure'].astype('int')
            
            scaled_data=preprocessor.transform(features)
           
            pred_score=model.predict(scaled_data)
           
            return pred_score[0]

        except Exception as e:
            raise CustomException(e,sys)
        
class CustomData:
    def __init__(self,
                 Gender:str,
                 Age:int,
                 Occupation:str,
                 Sleep_Duration:float,
                 Quality_of_Sleep:int,
                 Physical_Activity_Level:int,
                 Stress_Level:int,
                 BMI_Category:str,
                 Blood_Pressure:str,
                 Heart_Rate:int,
                 Daily_Steps:int
                 ):
        self.Gender=Gender
        self.Age=Age
        self.Occupation=Occupation
        self.Sleep_Duration=Sleep_Duration
        self.Quality_of_Sleep=Quality_of_Sleep
        self.Physical_Activity_Level=Physical_Activity_Level
        self.Stress_Level=Stress_Level
        self.BMI_Category=BMI_Category
        self.Blood_Pressure=Blood_Pressure
        self.Heart_Rate=Heart_Rate
        self.Daily_Steps=Daily_Steps
    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict={
                "Gender":[self.Gender],
                "Age":[self.Age],
                "Occupation":[self.Occupation],
                "Sleep_Duration":[self.Sleep_Duration],
                "Quality_of_Sleep":[self.Quality_of_Sleep],
                "Physical_Activity_Level":[self.Physical_Activity_Level],
                "Stress_Level":[self.Stress_Level],
                "BMI_Category":[self.BMI_Category],
                "Blood_Pressure":[self.Blood_Pressure],
                "Heart_Rate":[self.Heart_Rate],
                "Daily_Steps":[self.Daily_Steps]
            }
            return pd.DataFrame(custom_data_input_dict)
        except Exception as e:
            raise CustomException(e,sys)
