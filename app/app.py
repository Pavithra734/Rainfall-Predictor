from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("../model/best_model.pkl","rb"))
scaler = pickle.load(open("../model/scaler.pkl","rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    features = [
        float(request.form['MinTemp']),
        float(request.form['MaxTemp']),
        float(request.form['Rainfall']),
        float(request.form['Humidity9am']),
        float(request.form['Humidity3pm'])
    ]

    final = scaler.transform([features])
    prediction = model.predict(final)[0]

    result = "Rain Expected ☔" if prediction==1 else "No Rain 🌤"

    return render_template("result.html", prediction=result)

if __name__ == "__main__":
    app.run(debug=True)
