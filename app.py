from flask import Flask, request, jsonify
from src.predict import predict_churn

app = Flask(__name__)

@app.route("/")
def home():
    return "Customer Churn API Running"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json["features"]
        pred = predict_churn(data)

        result = "Customer will Churn" if pred == 1 else "Customer will Stay"

        return jsonify({"prediction": result})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
