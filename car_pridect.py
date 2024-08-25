
import streamlit as st
import joblib
import pandas as pd

# Load the entire fitted pipeline
pipeline = joblib.load('model_pipeline.pkl')

# Define the title of the app
st.title("Car Resale Price Prediction")

# Create input fields for all required features
registered_year = st.slider("Registered Year", min_value=2005, max_value=2024, value=2015)
engine_capacity = st.slider("Engine Capacity (cc)", min_value=750, max_value=2000, value=1200)
kms_driven = st.slider("KMs Driven", min_value=0, max_value=200000, value=50000)
max_power = st.slider("Max Power (bhp)", min_value=30, max_value=200, value=85)
seats = st.slider("Seats", min_value=2, max_value=10, value=5)
mileage = st.slider("Mileage (kmpl)", min_value=5.0, max_value=50.0, value=20.0)

insurance = st.selectbox("Insurance", ["Comprehensive insurance", "Third Party insurance"])
transmission_type = st.selectbox("Transmission Type", ["Manual", "Automatic"])
owner_type = st.selectbox("Owner Type", ["First Owner", "Second Owner", "Third Owner", "Fourth & Above Owner"])
fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG", "LPG", "Electric"])
body_type = st.selectbox("Body Type", ["Hatchback", "Sedan", "SUV"])
city = st.selectbox("City", ["Agra", "Delhi", "Mumbai", "Chennai", "Kolkata", "Bangalore", "Pune"])
company_name = st.selectbox("company_name", ['Maruti','Hyundai','Honda','Tata','Renault','Volkswagen','Ford','Toyota','Skoda','Nissan', 'Kia', 'Chevrolet','Mahindra','Datsun','Fiat'])


# Construct the input data for all features, with each value in a list to represent a single row
input_data = {
    'registered_year': [registered_year],
    'engine_capacity(CC)': [engine_capacity],
    'kms_driven': [kms_driven],
    'max_power(bhp)': [max_power],
    'seats': [seats],
    'mileage': [mileage],
    'insurance': [insurance],
    'transmission_type': [transmission_type],
    'owner_type': [owner_type],
    'fuel_type': [fuel_type],
    'body_type': [body_type],
    'city': [city],
    'company_name':['company_name']
}

# Convert input_data to a DataFrame
input_df = pd.DataFrame(input_data)

# Add a button to predict
if st.button("Predict Price"):
    # Make a prediction using the entire pipeline
    prediction = pipeline.predict(input_df)
    
    # Display the prediction
    st.success(f"The predicted resale price is {prediction[0]:,.2f}")

# Add a reset button to clear inputs
if st.button("Reset"):
    st.experimental_rerun()
