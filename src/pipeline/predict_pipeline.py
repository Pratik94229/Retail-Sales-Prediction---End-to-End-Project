import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object
import os


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)



class CustomData:
    def __init__(self,
                 store: int,
                 day_of_week: int,
                 date: str,
                 sales: int,
                 customers: int,
                 open: int,
                 promo: int,
                 state_holiday: str,
                 school_holiday: int,
                 store_type: str,
                 assortment: str,
                 competition_distance: float,
                 competition_open_since_month: int,
                 competition_open_since_year: int,
                 promo2: int,
                 promo2_since_week: int,
                 promo2_since_year: int,
                 promo_interval: str):

   
        self.store = store
        self.day_of_week = day_of_week
        self.date = date
        self.sales = sales
        self.customers = customers
        self.open = open
        self.promo = promo
        self.state_holiday = state_holiday
        self.school_holiday = school_holiday
        self.store_type = store_type
        self.assortment = assortment
        self.competition_distance = competition_distance
        self.competition_open_since_month = competition_open_since_month
        self.competition_open_since_year = competition_open_since_year
        self.promo2 = promo2
        self.promo2_since_week = promo2_since_week
        self.promo2_since_year = promo2_since_year
        self.promo_interval = promo_interval

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
              
                "store": [self.store],
                "day_of_week": [self.day_of_week],
                "date": [self.date],
                "sales": [self.sales],
                "customers": [self.customers],
                "open": [self.open],
                "promo": [self.promo],
                "state_holiday": [self.state_holiday],
                "school_holiday": [self.school_holiday],
                "store_type": [self.store_type],
                "assortment": [self.assortment],
                "competition_distance": [self.competition_distance],
                "competition_open_since_month": [self.competition_open_since_month],
                "competition_open_since_year": [self.competition_open_since_year],
                "promo2": [self.promo2],
                "promo2_since_week": [self.promo2_since_week],
                "promo2_since_year": [self.promo2_since_year],
                "promo_interval": [self.promo_interval]
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)
