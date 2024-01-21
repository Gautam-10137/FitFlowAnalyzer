import pandas as pd
import os
import sys
from src.logger import logging
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder,StandardScaler,LabelEncoder
from sklearn.pipeline import Pipeline

from src.utils import save_object

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
                    ("onehot_encoder",OneHotEncoder()),
                   
                ]
            )
            target_pipeline = Pipeline(
                steps=[
                    ("onehot_encoder", OneHotEncoder(), [target_column])
                ]
            )

            preprocessor=ColumnTransformer(
                [

                    ("num_pipelines",num_pipeline,numerical_columns),
                    ("cat_pipelines",cat_pipeline,categorical_columns),
                    # ("target_pipeline",target_pipeline,[target_column])
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
            # print(numerical_columns)
            # print(categorical_columns)
            target_column="Sleep_Disorder"
            categorical_columns=[column for column in categorical_columns if column!=target_column]
            # print(categorical_columns)
            logging.info("Obtaining preprocessing object")
            preprocessor_obj=self.get_data_transformation_config(numerical_columns,categorical_columns,target_column)


            input_feature_train_df=train_data.drop(columns=[target_column],axis=1)
            input_feature_test_df=test_data.drop(columns=[target_column],axis=1)
            
            target_feature_train=train_data[target_column]
            target_feature_test=test_data[target_column]
            # target_feature_train=pd.DataFrame(target_feature_train,columns=[target_column])
            # target_feature_test=pd.DataFrame(target_feature_test,columns=[target_column])

            logging.info("Applying preprocessing object on training dataframe and testing dataframe")

            input_feature_train_arr=preprocessor_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessor_obj.transform(input_feature_test_df)
            logging.info("Applied Preprocessing on input features")
            # Apply preprocessing to the target column
            # Mapping the categories
            sleep_map={'No Disorder':0,'Sleep Apnea':1,'Insomnia':2}

            target_column_train_values =target_feature_train.map(sleep_map).astype('int')
            
            target_column_test_values =target_feature_test.map(sleep_map).astype('int')
            
            target_column_train_arr=target_column_train_values.values.reshape(-1, 1)
            target_column_test_arr=target_column_test_values.values.reshape(-1, 1)
            print(target_column_train_arr[0,0].dtype)

            # imputer = SimpleImputer(strategy="most_frequent")
            # onehot_encoder = OneHotEncoder()

            # target_column_train_arr =onehot_encoder.fit_transform(
            #     imputer.fit_transform(target_feature_train.values.reshape(-1, 1))
            # ).toarray()
            # target_column_test_arr = onehot_encoder.fit_transform(
            #     imputer.fit_transform(target_feature_test.values.reshape(-1, 1))
            # ).toarray()
            
            train_arr = np.column_stack((input_feature_train_arr, target_column_train_arr.astype('int')))
            test_arr = np.column_stack((input_feature_test_arr, target_column_test_arr.astype('int')))
            # print(train_arr.dtype)
            # print(test_arr.dtype)
           
            train_arr[:,-1 ]=train_arr[:,-1 ].astype('int')
            test_arr[:,-1 ]=test_arr[:,-1 ].astype('int')
            
            # print(test_arr[0])
            logging.info("Saving preprocessing object")
            save_object(
                file_path=self.transformationConfig.preprocessor_file_path,
                obj=preprocessor_obj
            )

            logging.info("Saved preprocessing object")
            
            return (
                train_arr,
                test_arr,
                self.transformationConfig.preprocessor_file_path
            )
        except Exception as e:
            raise CustomException(e,sys)

