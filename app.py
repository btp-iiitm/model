from flask import Flask, request, jsonify

import predict_grade

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to the Predicting Api!, It's open for all users."


@app.route("/api/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        data = request.get_json()
        return jsonify(predict_grade.predict(data))
