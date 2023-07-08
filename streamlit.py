import streamlit as st
import pandas as pd
import pickle

# Load the preprocessor
with open('artifacts/proprocessor.pkl', 'rb') as f:
    preprocessor = pickle.load(f)

# Load the model
with open('artifacts/model.pkl', 'rb') as f:
    model = pickle.load(f)

# Create the Streamlit web app
def main():
    try:
        st.title("Retail Sales Prediction")

    # Upload and preprocess data
        uploaded_file = st.file_uploader("Upload CSV file", type="csv")
        if uploaded_file is not None:
            data = pd.read_csv(uploaded_file)
            preprocessed_data = preprocess_data(data)
            predictions = make_predictions(preprocessed_data)
            display_predictions(predictions, data)
    except:
        st.write("Enter correct csv file")        

def preprocess_data(data):
    # Select the required columns
    columns = ['Store', 'DayOfWeek', 'Date', 'Sales', 'Customers', 'Open', 'Promo',
               'StateHoliday', 'SchoolHoliday', 'StoreType', 'Assortment',
               'CompetitionDistance', 'CompetitionOpenSinceMonth',
               'CompetitionOpenSinceYear', 'Promo2', 'Promo2SinceWeek',
               'Promo2SinceYear', 'PromoInterval']
    data = data[columns]

    # Preprocess the data using the preprocessor
    preprocessed_data = preprocessor.transform(data)

    return preprocessed_data

def make_predictions(data):
    # Make predictions using the model
    predictions = model.predict(data)

    return predictions

def display_predictions(predictions, data):
   
        # Display the expected sales values along with store number and date
        result_df = pd.DataFrame({
            'Store': data['Store'],
            'Date': pd.to_datetime(data['Date']),
            'Expected Sales': predictions})

        st.write(result_df)
       

if __name__ == '__main__':
    main()
