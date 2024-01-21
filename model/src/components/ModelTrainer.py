import os
import sys
from src.logger import logging
from src.exception import CustomException
from dataclasses import dataclass
from src.utils import evaluate_models
from src.utils import save_object
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from catboost import CatBoostClassifier
from xgboost import XGBClassifier
from sklearn.svm import SVC
from sklearn.metrics import r2_score

@dataclass
class ModelTrainerConfig:
    trained_model_file_path:str=os.path.join("artifacts","model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()
    
    def initiate_model_trainer(self,train_arr,test_arr):
        logging.info("Entered model training component")
        try:
            logging.info("Split training ans test data")
            X_train,y_train,X_test,y_test=(train_arr[:,:-1],train_arr[:,-1],test_arr[:,:-1],test_arr[:,-1])
            # y_train=y_train[:]
            y_train=y_train[:].astype('int')
            y_test=y_test[:].astype('int')
            # print(y_train.dtype)
            models={
                "Random Forest": RandomForestClassifier(),
                "Gradient Boosting": GradientBoostingClassifier(),
                "Logistic Regression": LogisticRegression(),
                "XGBClassifier": XGBClassifier(),
                "SVM": SVC()
            }

            params={
                "Random Forest":{
                    'n_estimators': [50, 100, 200],
                    # 'max_depth': [None, 5, 10],
                    # 'min_samples_split': [2, 5, 10],
                    # 'min_samples_leaf': [1, 2, 4]
                },
                "Gradient Boosting":{
                    'n_estimators': [50, 100, 200],
                    'learning_rate': [0.01, 0.1, 0.2],
                    'max_depth': [3, 5, 7],
                    # 'min_samples_split': [2, 5, 10],
                    # 'min_samples_leaf': [1, 2, 4]   
                },
                "Logistic Regression":{
                    'penalty': ['l2'],
                    'C': [0.1, 1.0],
                    'solver': ['liblinear'],
                    'max_iter': [100]
                },
                "XGBClassifier":{
                    'n_estimators': [50, 100, 200],
                    'learning_rate': [0.01, 0.1, 0.2],
                    # 'max_depth': [3, 5, 7],
                    # 'min_child_weight': [1, 3, 5],
                    # 'subsample': [0.8, 1.0]                   
                },
                "SVM":{
                    'C': [0.1, 1.0, 10.0],
                    'kernel': ['linear', 'rbf'],
                    'gamma': ['scale', 'auto']
                }
            }

            model_report=evaluate_models(X_train,y_train,X_test,y_test,models,params)

            best_model_score=max(model_report.values())
            best_model_name=list(model_report.keys())[list(model_report.values()).index(best_model_score)]

            best_model=models[best_model_name]
            print(best_model_name)
            if best_model_score<0.6:
                raise CustomException("No best model Found")
            logging.info("Best model found on training and test dataset")
            save_object(
               file_path=self.model_trainer_config.trained_model_file_path,
               obj=best_model
            )
            # returning r2_score
            predicted_score=best_model.predict(X_test)
            r2_square=r2_score(y_test,predicted_score)
            return r2_square

        except Exception as e:
            raise CustomException(e,sys)