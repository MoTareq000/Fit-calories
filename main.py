from fastapi import FastAPI, Query
from pydantic import BaseModel
import xgboost as xgb
import numpy as np

app = FastAPI()

# Load model
model = xgb.Booster()
model.load_model("xgboost_model.json")

# ---- Root ----
@app.get("/")
def home():
    return {"message": "Calories Prediction API is running!"}

# ---- Input Schema for POST ----
class InputData(BaseModel):
    Gender: str
    Age: int
    Height: float
    Weight: float
    Duration: float
    Heart_Rate: float
    Body_Temp: float

# ---- Helper function ----
def make_prediction(gender, age, height, weight, duration, heart_rate, body_temp):
    gender_val = 1 if gender.lower() == "male" else 0
    input_data = np.array([[gender_val, age, height, weight, duration, heart_rate, body_temp]])

    feature_names = ["Gender", "Age", "Height", "Weight", "Duration", "Heart_Rate", "Body_Temp"]
    dtest = xgb.DMatrix(input_data, feature_names=feature_names)
    prediction = model.predict(dtest)
    return float(prediction[0])

# ---- GET endpoint ----
@app.get("/predict")
def predict_get(
    Gender: str,
    Age: int,
    Height: float,
    Weight: float,
    Duration: float,
    Heart_Rate: float,
    Body_Temp: float
):
    calories = make_prediction(Gender, Age, Height, Weight, Duration, Heart_Rate, Body_Temp)
    return {"calories_burned": calories}

# ---- POST endpoint ----
@app.post("/predict")
def predict_post(data: InputData):
    calories = make_prediction(
        data.Gender,
        data.Age,
        data.Height,
        data.Weight,
        data.Duration,
        data.Heart_Rate,
        data.Body_Temp
    )
    return {"calories_burned": calories}
