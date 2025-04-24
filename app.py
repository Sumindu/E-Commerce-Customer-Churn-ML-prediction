from flask import Flask, request, render_template
import joblib
import pandas as pd
import numpy as np
import datetime

app = Flask(__name__)

# Load the trained model
model = joblib.load('rf_churn_model.pkl')
print("Model loaded successfully.")

# Define feature columns (must match the one-hot encoded training data from the notebook)
feature_cols = [
    'Tenure', 'CityTier', 'WarehouseToHome', 'HourSpendOnApp', 'NumberOfDeviceRegistered',
    'SatisfactionScore', 'NumberOfAddress', 'Complain', 'OrderAmountHikeFromlastYear',
    'CouponUsed', 'OrderCount', 'DaySinceLastOrder', 'CashbackAmount',
    'PreferredLoginDevice_Mobile Phone', 'PreferredLoginDevice_Phone',
    'PreferredPaymentMode_COD', 'PreferredPaymentMode_Cash on Delivery',
    'PreferredPaymentMode_Credit Card', 'PreferredPaymentMode_Debit Card',
    'PreferredPaymentMode_E wallet', 'PreferredPaymentMode_UPI', 'Gender_Male',
    'MaritalStatus_Married', 'MaritalStatus_Single', 'PreferedOrderCat_Grocery',
    'PreferedOrderCat_Laptop & Accessory', 'PreferedOrderCat_Mobile',
    'PreferedOrderCat_Mobile Phone', 'PreferedOrderCat_Others'
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    # In a production environment, you would fetch real data from a database here
    # For demo purposes, we're just rendering the dashboard template with mock data
    return render_template('dashboard.html')
    
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        input_data = {
            'Tenure': float(request.form['Tenure']),
            'CityTier': int(request.form['CityTier']),
            'WarehouseToHome': float(request.form['WarehouseToHome']),
            'HourSpendOnApp': float(request.form['HourSpendOnApp']),
            'NumberOfDeviceRegistered': int(request.form['NumberOfDeviceRegistered']),
            'SatisfactionScore': int(request.form['SatisfactionScore']),
            'NumberOfAddress': int(request.form['NumberOfAddress']),
            'Complain': int(request.form['Complain']),
            'OrderAmountHikeFromlastYear': float(request.form['OrderAmountHikeFromlastYear']),
            'CouponUsed': float(request.form['CouponUsed']),
            'OrderCount': float(request.form['OrderCount']),
            'DaySinceLastOrder': float(request.form['DaySinceLastOrder']),
            'CashbackAmount': float(request.form['CashbackAmount']),
            'PreferredLoginDevice': request.form['PreferredLoginDevice'],
            'PreferredPaymentMode': request.form['PreferredPaymentMode'],
            'Gender': request.form['Gender'],
            'MaritalStatus': request.form['MaritalStatus'],
            'PreferedOrderCat': request.form['PreferedOrderCat']
        }

        # Convert input data to DataFrame
        input_df = pd.DataFrame([input_data])

        # Perform one-hot encoding on categorical variables
        input_df_encoded = pd.get_dummies(input_df, columns=[
            'PreferredLoginDevice', 'PreferredPaymentMode', 'Gender', 'MaritalStatus', 'PreferedOrderCat'
        ])

        # Ensure all required feature columns are present, filling missing ones with 0
        for col in feature_cols:
            if col not in input_df_encoded.columns:
                input_df_encoded[col] = 0

        # Reorder columns to match the training data
        input_df_encoded = input_df_encoded[feature_cols]

        # Convert to integer type to match training data
        input_df_encoded = input_df_encoded.astype(int)

        # Make prediction
        prediction = model.predict(input_df_encoded)[0]
        probability = model.predict_proba(input_df_encoded)[0][1]  # Probability of churn (class 1)

        # Determine result
        result = 'Churn' if prediction == 1 else 'No Churn'
        
        # Render result page
        return render_template('result.html', prediction=result, probability=f'{probability:.2%}')

    except Exception as e:
        # Handle errors and display them on the result page
        return render_template('result.html', prediction="Error", probability=str(e))

if __name__ == '__main__':
    app.run(debug=True)