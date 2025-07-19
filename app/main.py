# app/main.py

import streamlit as st
import numpy as np
import pickle

# Load model and scaler
with open('model/life_expectancy_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('model/scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

# Page config
st.set_page_config(page_title="Life Expectancy & Sleep Predictor", layout="centered")

st.title("🧬 Life Expectancy & Sleep Calculator")

st.markdown("Enter your details below:")

# Input fields
status = st.selectbox("Country Status", ["Developing", "Developed"])
adult_mortality = st.number_input("Adult Mortality (per 1000)", min_value=0)
infant_deaths = st.number_input("Infant Deaths", min_value=0)
alcohol = st.number_input("Alcohol Consumption (liters/year)", min_value=0.0)
bmi = st.number_input("BMI", min_value=10.0, max_value=60.0)
under_five_deaths = st.number_input("Under-Five Deaths", min_value=0)
polio = st.number_input("Polio Vaccination (%)", min_value=0.0, max_value=100.0)
total_expenditure = st.number_input("Health Expenditure (% of GDP)", min_value=0.0)
income_composition = st.slider("Income Composition of Resources", 0.0, 1.0)
schooling = st.slider("Schooling (years)", 0.0, 20.0)
sleep_hours = st.slider("Sleep Hours per Day", 4, 12, value=8)

# Prepare the input vector
if st.button("Predict"):
    status_num = 1 if status == "Developed" else 0

    input_data = np.array([[
        adult_mortality,
        infant_deaths,
        alcohol,
        bmi,
        under_five_deaths,
        polio,
        total_expenditure,
        status_num,
        income_composition,
        schooling
    ]])

    input_scaled = scaler.transform(input_data)
    predicted_life_expectancy = model.predict(input_scaled)[0]

    # Calculate total sleep
    total_sleep_days = predicted_life_expectancy * sleep_hours * 365.25 / 24

    st.success(f"🧓 Predicted Life Expectancy: **{predicted_life_expectancy:.2f} years**")
    st.info(f"😴 Estimated Total Lifetime Sleep: **{total_sleep_days:.0f} days**")
