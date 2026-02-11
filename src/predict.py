import joblib
import numpy as np

# Load saved artifacts
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

def predict_churn(features_list):
    """
    features_list order:
    [tenure, MonthlyCharges, SupportCalls, Contract, InternetService, TotalCharges]
    """

    data = np.array(features_list).reshape(1, -1)
    data_scaled = scaler.transform(data)
    prediction = model.predict(data_scaled)[0]

    return int(prediction)
