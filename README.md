# E-Commerce Customer Churn Prediction Platform

![E-Commerce Analytics](https://img.shields.io/badge/E--Commerce-Analytics-4361ee)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Random%20Forest-green)
![Flask](https://img.shields.io/badge/Framework-Flask-lightgrey)
![Bootstrap](https://img.shields.io/badge/UI-Bootstrap%205-purple)
![Version](https://img.shields.io/badge/Version-1.0.0-blue)

A sophisticated, enterprise-grade web application for predicting customer churn in e-commerce platforms. This solution leverages machine learning to identify customers at risk of churning, enabling businesses to take proactive retention measures.

<p align="center">
  <img src="https://via.placeholder.com/800x400?text=E-Commerce+Churn+Prediction+Platform" alt="E-Commerce Churn Prediction Platform" />
</p>

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Machine Learning Model](#machine-learning-model)
- [Input Features](#input-features)
- [Dashboard Analytics](#dashboard-analytics)
- [API Endpoints](#api-endpoints)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

## 🔭 Overview

The E-Commerce Customer Churn Prediction Platform is an advanced web application designed to help e-commerce businesses identify and predict customer churn. By analyzing various customer behavior patterns and attributes, the platform uses machine learning to forecast which customers are likely to stop using the service.

This predictive capability enables businesses to implement targeted retention strategies, improve customer satisfaction, and ultimately increase revenue by reducing customer attrition.

## ✨ Features

- **Customer Churn Prediction**: Accurately predicts the likelihood of a customer churning based on their behavior and profile data
- **Intuitive Data Entry**: User-friendly form with organized sections for customer profile, shopping behavior, and satisfaction metrics
- **Visual Result Display**: Clear visual representation of prediction results with probability indicator
- **Comprehensive Dashboard**: Detailed analytics dashboard with churn trends, customer distribution, and risk factors
- **Responsive Design**: Fully responsive UI that works seamlessly on desktop, tablet, and mobile devices
- **Error Handling**: Robust error handling with user-friendly error messages

## 🛠️ Technology Stack

### Backend
- **Python 3.8+**: Core programming language
- **Flask 2.0.1**: Web framework for building the application
- **Pandas 1.3.3**: Data manipulation and analysis
- **NumPy 1.21.2**: Numerical computing
- **Scikit-learn 0.24.2**: Machine learning library
- **Joblib 1.0.1**: Model persistence and loading

### Frontend
- **HTML5/CSS3**: Structure and styling
- **Bootstrap 5**: Frontend framework for responsive design
- **Chart.js**: JavaScript library for interactive data visualization
- **Font Awesome**: Icon library
- **JavaScript/jQuery**: Client-side interactivity and animations

## 📁 Project Structure

```
webApp/
│
├── app.py                  # Main Flask application file
├── requirements.txt        # Project dependencies
├── rf_churn_model.pkl      # Pre-trained Random Forest model
├── README.md               # Project documentation (this file)
├── .gitignore              # Git ignore file
│
└── templates/              # HTML templates
    ├── index.html          # Main page with data entry form
    ├── result.html         # Prediction results page
    └── dashboard.html      # Analytics dashboard
```

## 🚀 Installation

Follow these steps to set up the project locally:

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/ecommerce-churn-prediction.git
cd ecommerce-churn-prediction
```

2. **Create a virtual environment**

```bash
python -m venv venv
```

3. **Activate the virtual environment**

On Windows:
```bash
venv\Scripts\activate
```

On macOS/Linux:
```bash
source venv/bin/activate
```

4. **Install dependencies**

```bash
pip install -r requirements.txt
```

5. **Run the application**

```bash
python app.py
```

6. **Access the application**

Open your web browser and navigate to:
```
http://127.0.0.1:5000/
```

## 📊 Usage

### Data Entry Form

1. Navigate to the home page
2. Fill in all required fields with customer data:
   - **Customer Profile**: Tenure, City Tier, Gender, Marital Status
   - **Shopping Behavior**: Warehouse distance, App usage, Login device, etc.
   - **Order Details**: Order count, Days since last order, Cashback amount, etc.
   - **Satisfaction Metrics**: Satisfaction score, Complaints

3. Submit the form to generate a prediction

### Viewing Results

After submitting the form, the application will process the data and display:

- Churn prediction (Churn/No Churn)
- Probability percentage
- Visual indicator of risk level
- Recommendations based on the prediction

### Accessing the Dashboard

1. Click on "Dashboard" in the navigation menu
2. View comprehensive analytics including:
   - Customer distribution
   - Churn rate trends
   - Risk factors
   - City tier and product category analysis
   - Recent predictions

## 🧠 Machine Learning Model

The application uses a Random Forest classification model to predict customer churn. The model was trained on historical e-commerce customer data with the following characteristics:

- **Algorithm**: Random Forest Classifier
- **Training Data**: Historical customer behavior and churn status
- **Validation Method**: Cross-validation
- **Features**: 29 input features after one-hot encoding
- **Target Variable**: Binary (Churn/No Churn)

## 📝 Input Features

The prediction model uses the following customer attributes:

### Numerical Features
- **Tenure**: Duration of customer relationship (months)
- **CityTier**: Classification of the city (1, 2, or 3)
- **WarehouseToHome**: Distance from warehouse to customer's home (km)
- **HourSpendOnApp**: Time spent on application (hours)
- **NumberOfDeviceRegistered**: Number of devices registered
- **SatisfactionScore**: Customer satisfaction rating (1-5)
- **NumberOfAddress**: Number of addresses saved
- **Complain**: Whether customer has complained (0/1)
- **OrderAmountHikeFromlastYear**: Percentage increase in order amount
- **CouponUsed**: Number of coupons used
- **OrderCount**: Number of orders placed
- **DaySinceLastOrder**: Days since last order
- **CashbackAmount**: Cashback amount received

### Categorical Features
- **PreferredLoginDevice**: Preferred device for login
- **PreferredPaymentMode**: Preferred payment method
- **Gender**: Customer's gender
- **MaritalStatus**: Customer's marital status
- **PreferedOrderCat**: Preferred product category

## 📈 Dashboard Analytics

The dashboard provides comprehensive analytics including:

### Key Metrics
- Total customer count
- Active customers
- At-risk customers
- Churned customers

### Visualizations
- **Churn Rate Trend**: Monthly churn rate over time
- **Customer Distribution**: Percentage breakdown of customer status
- **City Tier Analysis**: Churn rates by city tier
- **Product Category Analysis**: Churn rates by preferred product category

### Risk Factor Table
The dashboard highlights top churn risk factors with impact levels and correlation strengths.

### Recent Predictions
Displays a log of recent churn predictions made by the system.

## 🔌 API Endpoints

The application provides the following endpoints:

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Home page with data entry form |
| `/predict` | POST | Processes input data and returns prediction |
| `/dashboard` | GET | Analytics dashboard |

## 🔮 Future Enhancements

Planned improvements for future versions:

1. **User Authentication**: Secure login system for different user roles
2. **Database Integration**: Store predictions and customer data for historical analysis
3. **Export Functionality**: Allow exporting of results and reports
4. **Model Retraining**: Automated model retraining with new data
5. **Advanced Analytics**: Cohort analysis and customer segmentation
6. **API Expansion**: RESTful API for integrating with other systems
7. **Multiple Models**: Support for different prediction algorithms
8. **Recommendation Engine**: Personalized retention strategy recommendations

## 👥 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


---

<p align="center">
  Developed with ❤️ by Sumindu Ekanayaka | © 2025 E-Commerce Analytics
</p>