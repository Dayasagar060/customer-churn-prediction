from flask import Flask, render_template, request
import pandas as pd
import joblib
from pathlib import Path

app = Flask(__name__)

# Project directory
BASE_DIR = Path(__file__).resolve().parent

# Load trained model
model = joblib.load(
    BASE_DIR / "models" / "best_churn_pipeline.pkl"
)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    # Get data from HTML form
    credit_score = float(request.form["credit_score"])
    country = request.form["country"]
    gender = request.form["gender"]
    age = float(request.form["age"])
    tenure = float(request.form["tenure"])
    balance = float(request.form["balance"])
    products_number = float(request.form["products_number"])
    credit_card = int(request.form["credit_card"])
    active_member = int(request.form["active_member"])
    estimated_salary = float(request.form["estimated_salary"])

    # Create DataFrame
    df = pd.DataFrame([{
        "credit_score": credit_score,
        "country": country,
        "gender": gender,
        "age": age,
        "tenure": tenure,
        "balance": balance,
        "products_number": products_number,
        "credit_card": credit_card,
        "active_member": active_member,
        "estimated_salary": estimated_salary
    }])

    # Feature engineering
    df["balance_per_product"] = (
        df["balance"] / df["products_number"]
    )

    df["salary_balance_ratio"] = (
        df["estimated_salary"] / (df["balance"] + 1)
    )

    df["age_group"] = pd.cut(
        df["age"],
        bins=[0, 30, 40, 50, 100],
        labels=[
            "Young",
            "Adult",
            "Middle_Age",
            "Senior"
        ]
    )

    df["tenure_bucket"] = pd.cut(
        df["tenure"],
        bins=[-1, 2, 5, 10],
        labels=[
            "New",
            "Medium",
            "Long"
        ]
    )

    df["high_balance"] = (
        df["balance"] > 100000
    ).astype(int)

    # Prediction
    prediction = model.predict(df)[0]

    probability = model.predict_proba(df)[0][1]

    if prediction == 1:
        result = "Customer is likely to churn"
    else:
        result = "Customer is unlikely to churn"

    return f"""
    <!DOCTYPE html>
    <html>

    <head>
        <title>Prediction Result</title>

        <style>
            body {{
                font-family: Arial, sans-serif;
                text-align: center;
                background-color: #f4f6f8;
                padding-top: 100px;
            }}

            .result {{
                background: white;
                max-width: 500px;
                margin: auto;
                padding: 40px;
                border-radius: 10px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            }}

            h1 {{
                margin-bottom: 30px;
            }}

            .prediction {{
                font-size: 24px;
                font-weight: bold;
                margin-bottom: 20px;
            }}

            .probability {{
                font-size: 20px;
                margin-bottom: 30px;
            }}

            a {{
                text-decoration: none;
                color: #007bff;
            }}
        </style>

    </head>

    <body>

        <div class="result">

            <h1>Prediction Result</h1>

            <div class="prediction">
                {result}
            </div>

            <div class="probability">
                Churn Probability:
                {probability:.2%}
            </div>

            <a href="/">
                ← Predict Another Customer
            </a>

        </div>

    </body>

    </html>
    """


if __name__ == "__main__":
    print("Customer Churn Prediction App is running!")
    app.run(debug=True)