import pandas as pd
import os
import sys
from src.logger import logging
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder,StandardScaler,LabelEncoder
from sklearn.pipeline import Pipeline

from src.exception import CustomException 
from dataclasses import dataclass

@dataclass
class DataTransformationConfig:
    preprocessor_file_path=os.path.join("artifacts","preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.transformationConfig=DataTransformationConfig()

    def get_data_transformation_config(self,numerical_columns,categorical_columns,target_column):
        logging.info("Entered the data transformstion components")
        try:
            num_pipeline=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="median")),
                    ("scaler",StandardScaler(with_mean=False))
                ]
            )
            cat_pipeline=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="most_frequent")),
                    ("label_encoder",OneHotEncoder()),
                   
                ]
            )

            preprocessor=ColumnTransformer(
                [
                    ("num_pipelines",num_pipeline,numerical_columns),
                    ("cate_pipelines",cat_pipeline,categorical_columns),
                    ("target_pipeline",OneHotEncoder(),[target_column])
                ]
            )
            return preprocessor
        except Exception as e:
            CustomException(e,sys)
    
    def initiate_data_transfomation(self,train_path,test_path):
        try:
            # task: transform data into appropriate fomr and make a transforer object so that we can transform input data, 
            # which we have to predict. 
            logging.info("Reading train and test data")
            train_data=pd.read_csv(train_path)
            test_data=pd.read_csv(test_path)

            numerical_columns=[feature for feature in train_data.columns if train_data[feature].dtype!='O']
            categorical_columns=[feature for feature in train_data.columns if train_data[feature].dtype=='O']

            target_column="Sleep Disorder"
            categorical_columns=[column for column in categorical_columns if column!=target_column]

            logging.info("Obtaining preprocessing object")
            preprocessor_obj=self.get_data_transformation_config(numerical_columns,categorical_columns,target_column)

            input_feature_train_df=train_data.drop(columns=[target_column],axis=1)
            input_feature_test_df=test_data.drop(columns=[target_column],axis=1)

            target_feature_train=train_data[target_column]
            target_feature_test=test_data[target_column]

            logging.info("Applying preprocessing object on training dataframe and testing dataframe")

            input_feature_train_arr=preprocessor_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessor_obj.transform(input_feature_test_df)
            target_feature_train_arr=preprocessor_obj.fit_transform(target_feature_train)
            target_feature_test_arr=preprocessor_obj.transform(target_feature_test)
            train_arr=np.c_[input_feature_train_arr,target_feature_train_arr]
            test_arr=np.c_[input_feature_test_arr,target_feature_test_arr]

            # save_object(
            #     file_path=self.transformationConfig.preprocessor_file_path,
            #     obj=preprocessor_obj
            # )
            logging.info("Saved preprocessing object")
        except Exception as e:
            CustomException(e,sys)

