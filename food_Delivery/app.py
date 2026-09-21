import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("food_delivery_model.pkl")

st.title("🍔 Food Delivery Time Estimation")

st.write("Predict Food Delivery Time Using Machine Learning")

# Inputs
distance = st.number_input(
    "Distance (km)",
    min_value=0.0,
    value=5.0
)

weather = st.selectbox(
    "Weather",
    ["Clear", "Rainy", "Snowy", "Foggy", "Windy"]
)

traffic = st.selectbox(
    "Traffic Level",
    ["Low", "Medium", "High"]
)

time_of_day = st.selectbox(
    "Time of Day",
    ["Morning", "Afternoon", "Evening", "Night"]
)

vehicle = st.selectbox(
    "Vehicle Type",
    ["Bike", "Scooter", "Car"]
)

prep_time = st.number_input(
    "Preparation Time (minutes)",
    min_value=1,
    value=15
)

experience = st.number_input(
    "Courier Experience (years)",
    min_value=0,
    value=2
)

# Create input dataframe
input_df = pd.DataFrame({
    "Distance_km":[distance],
    "Weather":[weather],
    "Traffic_Level":[traffic],
    "Time_of_Day":[time_of_day],
    "Vehicle_Type":[vehicle],
    "Preparation_Time_min":[prep_time],
    "Courier_Experience_yrs":[experience]
})

# Apply same encoding used during training
input_df = pd.get_dummies(input_df)

# Align columns with training data
model_columns = joblib.load("model_columns.pkl")

input_df = input_df.reindex(
    columns=model_columns,
    fill_value=0
)

# Prediction
if st.button("Predict Delivery Time"):

    prediction = model.predict(input_df)

    st.success(
        f"Estimated Delivery Time: {prediction[0]:.2f} minutes"
    )
import streamlit as st
import pandas as pd
import joblib
import os

# Project folder path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load model files
model = joblib.load(os.path.join(BASE_DIR, "food_delivery_model.pkl"))
model_columns = joblib.load(os.path.join(BASE_DIR, "model_columns.pkl"))