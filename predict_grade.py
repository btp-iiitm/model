import joblib

le = joblib.load("labelencoder.pkl")
scaler = joblib.load("scaler.pkl")
model = joblib.load("model.pkl")


def predict(grades):
    grades_scaled = scaler.transform([list(grades.values())])
    predicted_grade_index = model.predict(grades_scaled)[0]
    predicted_grade = le.inverse_transform([predicted_grade_index])[0]

    return predicted_grade
