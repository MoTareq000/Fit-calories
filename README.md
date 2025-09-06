# 🥗 Fit Calories

**Fit Calories** is an end-to-end **Machine Learning deployment project** that predicts calories burned based on user activity.  
The project is deployed across **web** and **mobile**, making the model accessible in real time.

---

## 🚀 Features
- 🔥 Trained an ML model using **XGBoost**
- 📊 Model Performance: **R² = 0.96**, **MSE = 12.4**
- ⚡ Exposed via a **FastAPI backend** (deployed on Railway)
- 🌐 Interactive **Streamlit web app**
- 📱 **iOS Swift app** integration 

---

## 📂 Project Structure
├── api.py # FastAPI backend
├── app.py # Streamlit web app
├── xgboost_model.json # Trained ML model
├── requirements.txt # Dependencies
└── README.md

---

## ⚡ API 
[**Base URL**](https://web-production-252e7.up.railway.app/) :

streamlit website :

https://fit-calories-kqe4hd4scauohwrk86tbd8.streamlit.app/


### Endpoints
- **Root**: `/` → returns a status message  
- **Predict**: `/predict`  
  - Method: `POST`  
  - Body (JSON):
    ```json
    {
      "Gender": "Male",
      "Age": 25,
      "Height": 175,
      "Weight": 70,
      "Duration": 30,
      "Heart_Rate": 100,
      "Body_Temp": 37
    }
    ```
  - Response:
    ```json
    {
      "calories": 245.67
    }
    ```

---

## 🎯 Next Steps
- Improve accuracy with hyperparameter tuning  
- Add authentication for API  
- Deploy frontend and backend together  

---

## 👨‍💻 Contributors
 **[Ahmad Alshafie]** – iOS Swift App  
 **Mohamad tareq** – Machine Learning, API, Streamlit Web App  


---

#MachineLearning #FastAPI #Streamlit #iOS #XGBoost #Deployment #Railway #Collaboration

