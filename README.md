# Customer Churn Prediction

An end-to-end Machine Learning project that predicts whether a bank customer is likely to churn based on customer and account information.

## Project Overview

Customer churn is an important problem for banks because losing existing customers can impact revenue.

This project uses Machine Learning to predict customer churn and provides a Flask web application where users can enter customer details and receive a churn prediction with probability.

## Features

The model uses the following customer information:

* Credit Score
* Country
* Gender
* Age
* Tenure
* Balance
* Number of Products
* Credit Card
* Active Member
* Estimated Salary

### Engineered Features

Additional features were created during feature engineering:

* Balance per Product
* Salary Balance Ratio
* Age Group
* Tenure Bucket
* High Balance

## Machine Learning Workflow

```text
Data
  ↓
Data Cleaning
  ↓
Exploratory Data Analysis
  ↓
Feature Engineering
  ↓
Data Preprocessing
  ↓
Model Training
  ↓
Model Evaluation
  ↓
Best Model Selection
  ↓
Save ML Pipeline
  ↓
Flask Deployment
  ↓
HTML Web Interface
  ↓
Churn Prediction
```

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Flask
* HTML/CSS
* Joblib
* Jupyter Notebook

## Project Structure

```text
Customer Churn Prediction/
│
├── data/
│   └── customer_data.csv
│
├── models/
│   └── best_churn_pipeline.pkl
│
├── notebooks/
│   └── Analysis.ipynb
│
├── templates/
│   └── index.html
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Flask Web Application

The project includes a simple HTML interface for entering customer information.

The Flask backend:

1. Receives customer details from the HTML form.
2. Performs feature engineering.
3. Loads the trained Machine Learning pipeline.
4. Generates the churn prediction.
5. Calculates the churn probability.
6. Displays the prediction to the user.

## Example Prediction

```text
Prediction:
Customer is unlikely to churn

Churn Probability:
6.69%
```

## How to Run the Project

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

Windows:

```powershell
.venv\Scripts\activate
```

### 4. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 5. Run the Flask application

```powershell
python app.py
```

### 6. Open the application

Open your browser:

```text
http://127.0.0.1:5000/
```

## Model

The trained Machine Learning pipeline is saved as:

```text
models/best_churn_pipeline.pkl
```

## Future Improvements

* Deploy the application to the cloud
* Add Docker support
* Add automated testing
* Add CI/CD
* Add model monitoring
* Add model explainability using SHAP
* Improve the web interface

## Author

**Dayasagar**
