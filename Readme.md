# 📉 Customer Churn Prediction API

End-to-End Machine Learning Project to predict customer churn for a telecom company using Python, Scikit-Learn and Flask.

---

## 🎯 Project Objective

Customer churn is one of the biggest problems in telecom companies.  
Acquiring a new customer costs 5x more than retaining an existing one.

Goal of this project:
Build a Machine Learning model that predicts whether a customer is likely to **churn (leave the company)** so the business can take preventive action.

---

## 🧠 Business Use Case

This model helps companies:

• Identify high-risk customers  
• Launch retention campaigns  
• Reduce revenue loss  
• Improve customer satisfaction  

---

## 📊 Dataset Features

Synthetic telecom dataset created for ML training.

| Feature | Description |
|---|---|
| tenure | Months with the company |
| MonthlyCharges | Monthly bill amount |
| TotalCharges | Total money spent |
| SupportCalls | Number of complaints |
| Contract | Contract type |
| InternetService | Type of internet |
| Churn | Target variable (0/1) |

Target:
- 0 → Customer stays  
- 1 → Customer churns

---

## 🔬 Machine Learning Pipeline

1️⃣ Data Generation  
2️⃣ Data Preprocessing  
3️⃣ Encoding Categorical Features  
4️⃣ Feature Scaling  
5️⃣ Train/Test Split  
6️⃣ Model Training (Random Forest)  
7️⃣ Model Saving (Joblib)  
8️⃣ Flask API Deployment  

---

## 🤖 Model Used

Random Forest Classifier

Why Random Forest?
• Handles nonlinear relationships  
• Works well on tabular data  
• High accuracy with minimal tuning  

---

## 📈 Model Output

The API predicts:
- **Customer will Stay**
- **Customer will Churn**

---

## 🚀 Running the Project Locally

### Step 1 — Install Dependencies
pip install -r requirements.txt


### Step 2 — Generate Dataset


python create_dataset.py


### Step 3 — Train Model


python src/train_model.py


### Step 4 — Run Flask API


python app.py


Server runs at:


http://localhost:5000


---

## 🔗 API Usage

### Endpoint


POST /predict


### Request Body
{

    "features": [5, 80, 7, 0, 1, 400]

}


### Feature Order


[tenure, MonthlyCharges, SupportCalls, Contract, InternetService, TotalCharges]


Contract Encoding:
- Month = 0  
- One Year = 1  
- Two Year = 2  

Internet Service Encoding:
- DSL = 0  
- Fiber = 1  
- No Internet = 2  

### Response Example
{

    "prediction": "Customer will Churn"

}


---

## 🌍 Deployment

This API can be deployed on:
- Render
- Railway
- AWS
- Heroku  

---

## 🛠 Tech Stack

Python  
Scikit-Learn  
Pandas  
NumPy  
Flask  
Joblib  

---

## 📌 Future Improvements

• Use real telecom dataset  
• Add web UI dashboard  
• Add model monitoring  
• Add customer segmentation  

---

## 🌍 Live API Demo (Render Deployment)

The model is deployed as a public Flask API on Render.

Base URL

https://customer-churn-prediction-api-fzu9.onrender.com

---

## 🔗 Prediction Endpoint

POST /predict

### Sample Request
{

      "features": [5, 80, 7, 0, 1, 400]

}

### Sample Response
{
    
      "prediction": "Customer will Stay"

}

### 📸 Deployment Proof


<img width="851" height="1016" alt="image" src="https://github.com/user-attachments/assets/ea067c5e-1c3f-421c-af5d-74e40968ce2d" />





## 👨‍💻 Author

Shreyash Gade  

