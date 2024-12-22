import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
import os
from sklearn.metrics import accuracy_score as accuracy
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier, AdaBoostClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from xgboost import XGBClassifier
from src.utils import evaluate_models
from src.exception import CustomException
from src.utils import save_object
from dataclasses import dataclass
from src.logger import logging
import sys

@dataclass
class ModelTrainerConfig:
    traned_model_file_path=os.path.join('artifacts','model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()

    def initiate_model_trianer(self,train_array,test_array,preprocessor_path=None):
        try:
            logging.info("splitting_data")
            x_train,y_train,x_test,y_test=(train_array[:,:-1],
                                           train_array[:,-1],
                                           test_array[:,:-1],
                                           test_array[:,-1])
            models={"RandomForest":RandomForestClassifier(),
                    "KNeighborsClassifier" :KNeighborsClassifier(),
                    "DecisionTreeClassifier":DecisionTreeClassifier(),
                    "XGBClassifier":XGBClassifier(),
                    "GradientBoostingClassifier":GradientBoostingClassifier(),
                    "LogisticRegression":LogisticRegression()}
            model_report:dict=evaluate_models(x_train=x_train,y_train=y_train,x_test=x_test,y_test=y_test,models=models)
            best_model_score=max(sorted(model_report.values()))
            best_model_name=list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model=models[best_model_name]
            logging.info(f"best model found as {best_model}")
            save_object(
                file_path=self.model_trainer_config.traned_model_file_path,
                obj=best_model
            )
            predicted=best_model.predict(x_test)
            r2score=accuracy(y_test,predicted)
            return(r2score,best_model)
        except Exception as e:
            raise CustomException(e,sys)