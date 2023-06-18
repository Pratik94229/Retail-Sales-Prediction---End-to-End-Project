import sys
from dataclasses import dataclass

import numpy as np 
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import PowerTransformer, MinMaxScaler, OneHotEncoder

from src.exception import CustomException
from src.logger import logging
import os

from src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts',"proprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    def get_data_transformer_object(self):
           '''This function is responsible for data trnasformation'''
           try:
            # Define the columns for different transformations
            numeric_cols = ['Customers', 'CompetitionDistance', 'CompetitionOpenSinceYear']
            categorical_cols = ['PromoInterval', 'StoreType', 'Assortment']
            


            # Create a pipeline for numeric columns
            numeric_pipeline = Pipeline([('imputer', SimpleImputer(strategy='median')),
                                         ('power_transform', PowerTransformer(copy=False))])

            # Create a pipeline for categorical columns
            categorical_pipeline = Pipeline([('imputer', SimpleImputer(strategy='most_frequent')),
                                             ('onehot', OneHotEncoder())])

            # Combine the numeric and categorical pipelines using ColumnTransformer
            com_pipeline = ColumnTransformer([('numeric', numeric_pipeline, numeric_cols),
                                              ('categorical', categorical_pipeline, categorical_cols)])
            
            
        

            # Create the final pipeline
            preprocessor = Pipeline([('combined_pipeline', com_pipeline),('scaler', MinMaxScaler())])
            logging.info("Completed pipeline creation")

            return preprocessor

           except Exception as e:
              raise CustomException(e,sys)
        
    def initiate_data_transformation(self,train_path,test_path=None):

        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info("Read train and test data completed")

            logging.info("Obtaining preprocessing object")

            preprocessing_obj=self.get_data_transformer_object()

            target_column_name="Sales"
            '''numerical_columns = ['Store', 'DayOfWeek', 'Date', 'Sales', 'Customers', 'Open', 'Promo','StateHoliday', 
                                 'SchoolHoliday', 'StoreType', 'Assortment','CompetitionDistance', 'CompetitionOpenSinceMonth',
                                 'CompetitionOpenSinceYear', 'Promo2', 'Promo2SinceWeek','Promo2SinceYear', 'PromoInterval']'''

            input_feature_train_df=train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df=train_df[target_column_name]
            
            if(test_path):
                input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1)
                target_feature_test_df=test_df[target_column_name]
        

            logging.info(
                f"Applying preprocessing object on training dataframe and testing dataframe."
            )

            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)

            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            logging.info(f"Saved preprocessing object.")

            save_object(

                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj

            )

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )
        except Exception as e:
            raise CustomException(e,sys)
