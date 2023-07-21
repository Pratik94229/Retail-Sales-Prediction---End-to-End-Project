
# Retail Sales Prediction - End-to-End Regression Project

This repository contains code and resources for an end-to-end regression project on retail sales prediction. The goal of this project is to develop a regression model that can accurately predict retail sales based on various features.

## Dataset

The dataset used for this project contains the following columns:

- **Store**: The store ID.
- **DayOfWeek**: The day of the week (1-7, where 1 is Monday and 7 is Sunday).
- **Date**: The date of the sales record.
- **Sales**: The total sales for the given day and store.
- **Customers**: The number of customers on the given day and store.
- **Open**: Indicates whether the store was open (1) or closed (0) on the given day.
- **Promo**: Indicates whether a promotional offer was active (1) or not (0) on the given day.
- **StateHoliday**: Indicates whether the day was a state holiday (a, b, c) or not (0).
- **SchoolHoliday**: Indicates whether the day was a school holiday (1) or not (0).
- **StoreType**: The type of store (a, b, c, d).
- **Assortment**: The assortment level of the store (a = basic, b = extra, c = extended).
- **CompetitionDistance**: The distance to the nearest competitor store.
- **CompetitionOpenSinceMonth**: The month when the nearest competitor store opened.
- **CompetitionOpenSinceYear**: The year when the nearest competitor store opened.
- **Promo2**: Indicates whether a continuous promotional offer is active (1) or not (0).
- **Promo2SinceWeek**: The week of the year when the continuous promotional offer started.
- **Promo2SinceYear**: The year when the continuous promotional offer started.
- **PromoInterval**: The intervals at which the continuous promotional offer is repeated.

## Project Structure

The project structure is organized as follows:
```
├───artifacts
├───logs
├───notebook
│   └───data
├───src
│   ├───components
│   ├───pipeline
├───static
├───templates
```


- `notebook/`: Jupyter notebooks for data exploration, preprocessing, and model development.
- `notebook/data/`: contains the dataset file(s).
- `src/`: Source code for the project, including preprocessing functions and model training .
- `pipeline/`:Source code for different implemented pipelines.
- `artifacts/`: Directory to store model and evaluation results and perform predictions.
- `static/` and `templates/` contains basic frontend framework for deployment using flask.


## Getting Started

To get started with this project, you can follow these steps:

1. Clone the repository:

   ```
   git clone https://github.com/Pratik94229/Retail-Sales-Prediction---End-to-End-Project.git
   ```
2. Create virtual environment
   ```
   conda create -p venv python==3.8
   conda activate venv/
   ```

3. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Explore the collab notebooks in the `notebooks/` directory to understand the data and the steps involved in preprocessing and training the regression model.

5. Run the data ingestion script to preprocess,tranform the dataset along with training the model:

   ```
   python src/data_ingestion.py
   ```



6. Tune the model by changing parameters in model_trainer.py:

   ```
   python src/model_trainer.py
   ```

7. Run flask app by using 
`python app.py`


8. Streamlit deployment link https://pratik94229-retail-sales-prediction---end-to-e-streamlit-a7g08y.streamlit.app/

9. Load the desired file for predicting the result.

Feel free to modify the code and experiment with different models and techniques to improve the prediction accuracy.
## Acknowledgments

- The dataset used in this project is obtained from https://www.kaggle.com/competitions/rossmann-store-sales/data.


