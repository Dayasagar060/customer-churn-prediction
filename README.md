# Customer Churn Prediction

An end-to-end Machine Learning project that predicts whether a bank customer is likely to churn based on customer and account information.

## Project Overview

Customer churn is an important problem for banks because losing existing customers can impact revenue.

This project uses Machine Learning to predict customer churn and provides a Flask web application where users can enter customer details and receive a churn prediction with probability.

## Features

The model uses the following customer information:

- Credit Score
- Country
- Gender
- Age
- Tenure
- Balance
- Number of Products
- Credit Card
- Active Member
- Estimated Salary

### Engineered Features

Additional features were created during feature engineering:

- Balance per Product
- Salary Balance Ratio
- Age Group
- Tenure Bucket
- High Balance

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