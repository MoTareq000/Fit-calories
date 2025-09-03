import streamlit as st
import requests

st.title("Calories Burned Prediction")

gender = st.selectbox("Gender", ["male", "female"])
age = st.number_input("Age", min_value=1, max_value=120, value=25)
height = st.number_input("Height (cm)", value=175.0)
weight = st.number_input("Weight (kg)", value=70.0)
duration = st.number_input("Duration (minutes)", value=30.0)
heart_rate = st.number_input("Heart Rate", value=120.0)
body_temp = st.number_input("Body Temperature (°C)", value=37.0)

if st.button("Predict"):
    url = "https://web-production-252e7.up.railway.app/predict"
    params = {
        "Gender": gender,
        "Age": age,
        "Height": height,
        "Weight": weight,
        "Duration": duration,
        "Heart_Rate": heart_rate,
        "Body_Temp": body_temp
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        st.success(f"Calories burned: {response.json()['calories_burned']:.2f}")
    else:
        st.error("Error connecting to API")
