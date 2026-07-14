from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)

# Mock route to serve the homepage interface
@app.route('/')
def home():
    return render_template('index.html')

# Prediction endpoint processing incoming features
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract features submitted via the HTML form
        feat1 = float(request.form.get('feature1', 0))
        feat2 = float(request.form.get('feature2', 0))
        feat3 = float(request.form.get('feature3', 0))

        # In a real integration script, you load the saved model pickle file:
        # model = pickle.load(open('best_model.pkl', 'rb'))
        # prediction = model.predict([[feat1, feat2, feat3]])[0]

        # Simulating model inference confirmation for demonstration
        # prediction = "Process complete / Regular Transaction"
        # Feature 1 (Amount) 10000 కంటే ఎక్కువ ఇస్తే ఫ్రాడ్ అని చూపిస్తుంది
        if feat1 > 1000000:
               prediction = "Process complete / Fraudulent Transaction (High Risk)"
        else:
            prediction = "Process complete / Regular Transaction"

        return render_template('index.html', prediction=prediction)
    except Exception as e:
        return render_template('index.html', prediction=f"Error in processing: {str(e)}")

if __name__ == '__main__':
    # Running locally in development test environment
    print("Application backend is configured and ready.")
    app.run(debug=True)
