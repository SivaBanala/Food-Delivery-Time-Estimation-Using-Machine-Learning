🍔 Food Delivery Time Estimation Using Machine Learning
📌 Project Overview

This project aims to predict the food delivery time based on several operational factors such as distance, weather conditions, traffic levels, preparation time, vehicle type, courier experience, and time of day.

Accurate delivery time prediction helps food delivery companies improve customer satisfaction, optimize delivery operations, and provide realistic ETA (Estimated Time of Arrival) to customers.

🎯 Business Problem

Food delivery companies often face challenges in accurately estimating delivery times due to various dynamic factors.

The objective of this project is to:

Analyze factors affecting delivery time.
Build machine learning models to predict delivery time.
Compare different regression algorithms.
Generate business insights for operational improvements.
📂 Dataset Description
Feature	Description
Order_ID	Unique order identifier
Distance_km	Distance between restaurant and customer
Weather	Weather conditions (Clear, Rainy, Snowy, Foggy, Windy)
Traffic_Level	Traffic condition (Low, Medium, High)
Time_of_Day	Morning, Afternoon, Evening, Night
Vehicle_Type	Bike, Scooter, Car
Preparation_Time_min	Time required to prepare food
Courier_Experience_yrs	Delivery partner experience
Delivery_Time_min	Actual delivery time (Target Variable)
🎯 Target Variable
Delivery_Time_min

The goal is to predict the total delivery time in minutes.

🛠 Technologies Used
Python
Pandas
NumPy
Matplotlib
Seaborn
Scikit-Learn
📊 Data Preprocessing

The following preprocessing steps were performed:

Handling Missing Values
Weather → Mode Imputation
Traffic_Level → Mode Imputation
Time_of_Day → Mode Imputation
Courier_Experience_yrs → Median Imputation
Feature Engineering
Removed Order_ID
Applied One-Hot Encoding on categorical variables
Data Splitting
Train Size = 80%
Test Size = 20%
📈 Exploratory Data Analysis (EDA)
Univariate Analysis
Histogram of Delivery_Time_min
Boxplot of Delivery_Time_min
Bivariate Analysis
Distance vs Delivery Time
Weather vs Delivery Time
Traffic vs Delivery Time
Correlation Analysis

Heatmap was used to identify relationships between numerical variables.

🔍 Key EDA Findings
Distance
Strong positive correlation with delivery time.
Correlation = 0.78
Preparation Time
Moderate positive relationship.
Correlation = 0.31
Courier Experience
Weak negative relationship.
Correlation = -0.089
Weather Impact
Snowy weather produced the longest delivery times.
Rainy and Foggy conditions also increased delays.
Traffic Impact
High traffic significantly increased delivery duration.
🤖 Machine Learning Models

The following regression models were implemented and compared.

1️⃣ Simple Linear Regression
Input Feature
Distance_km
Purpose

Baseline model to understand how distance alone affects delivery time.

2️⃣ Multiple Linear Regression
Purpose

Uses all available features to predict delivery time.

Benefits
Easy to interpret
Provides feature importance through coefficients
3️⃣ Polynomial Regression
Degree
Degree = 2
Purpose

Captures:

Non-linear relationships
Feature interactions

Example:

Distance_km²
Distance_km × Preparation_Time_min
4️⃣ Ridge Regression
Purpose

Reduces overfitting by shrinking coefficients.

Advantage

Handles multicollinearity effectively.

5️⃣ Lasso Regression
Purpose

Performs automatic feature selection.

Advantage

Can remove less important features by assigning coefficient = 0.

6️⃣ Elastic Net Regression
Purpose

Combines:

Ridge Regression
Lasso Regression
Advantage

Balances feature selection and coefficient shrinkage.

📏 Evaluation Metrics

The models were evaluated using:

R² Score

Measures the proportion of variance explained by the model.

MAE (Mean Absolute Error)

Measures average prediction error.

RMSE (Root Mean Squared Error)

Measures overall prediction accuracy.

Cross Validation Score

Used to validate model stability.

📊 Feature Importance

The most influential features were:

Positive Impact on Delivery Time
Distance_km
Weather_Snowy
Weather_Foggy
Weather_Rainy
Preparation_Time_min
Negative Impact on Delivery Time
Traffic_Level_Low
Courier_Experience_yrs
📌 Business Insights
Insight 1

Distance is the strongest numerical predictor of delivery time.

Insight 2

Snowy, Foggy, and Rainy weather conditions significantly increase delivery delays.

Insight 3

High traffic conditions increase delivery duration considerably.

Insight 4

Orders with longer preparation times tend to have longer delivery times.

Insight 5

Experienced couriers complete deliveries slightly faster.

💡 Business Recommendations
Recommendation 1

Implement dynamic ETA calculations based on:

Distance
Weather
Traffic conditions
Recommendation 2

Assign experienced couriers during:

Peak traffic hours
Adverse weather conditions
Recommendation 3

Monitor restaurants with high preparation times to reduce delivery delays.

Recommendation 4

Integrate weather forecasting into ETA prediction systems.

🏆 Project Outcome

Successfully developed and compared multiple machine learning models for food delivery time estimation.

The project identified:

Distance
Weather Conditions
Traffic Levels
Preparation Time

as the most significant factors affecting delivery performance.

📌 Final Conclusion

This project demonstrates how machine learning can be used to accurately estimate food delivery times. Through extensive data analysis, feature engineering, and model comparison, the study found that weather conditions, traffic levels, distance, and preparation time have the greatest influence on delivery duration.

Among the tested models:

Multiple Linear Regression provided strong interpretability.
Polynomial Regression captured complex relationships and typically achieved the best predictive performance.
Ridge, Lasso, and Elastic Net improved model robustness through regularization techniques.

The final solution can help food delivery companies improve ETA accuracy, optimize logistics operations, and enhance customer satisfaction through data-driven decision-making.

👨‍💻 Author

Food Delivery Time Estimation Using Machine Learning
Regression-Based Machine Learning Project using Python & Scikit-Learn.

===============================================================================================================================================================

🚚 Food Delivery Time Estimation - Streamlit Web App
📌 Project Overview

This project is a Machine Learning-powered Streamlit Web Application that predicts food delivery times based on operational and environmental factors such as distance, weather conditions, traffic levels, vehicle type, preparation time, courier experience, and time of day.

The application helps logistics and food delivery companies estimate accurate delivery times, improve customer satisfaction, and optimize delivery operations.

🎯 Business Problem

Food delivery companies need accurate Estimated Time of Arrival (ETA) predictions to improve customer experience and operational efficiency.

This project predicts delivery time using historical delivery data and machine learning regression models.

📊 Dataset Features
Feature	Description
Distance_km	Delivery distance in kilometers
Weather	Weather condition during delivery
Traffic_Level	Traffic intensity (Low, Medium, High)
Time_of_Day	Morning, Afternoon, Evening, Night
Vehicle_Type	Bike, Scooter, Car
Preparation_Time_min	Order preparation time
Courier_Experience_yrs	Courier experience in years
Delivery_Time_min	Target variable
🛠️ Technologies Used
Python
Pandas
NumPy
Matplotlib
Seaborn
Scikit-Learn
Joblib
Streamlit
📈 Machine Learning Workflow
1. Data Preprocessing
Missing Value Treatment
Duplicate Removal
Feature Encoding
Feature Selection
2. Exploratory Data Analysis (EDA)
Target Variable Distribution
Correlation Heatmap
Scatter Plots
Box Plots
Feature Relationship Analysis
3. Model Development

Implemented and compared:

Simple Linear Regression
Multiple Linear Regression
Polynomial Regression
Ridge Regression
Lasso Regression
Elastic Net Regression
4. Model Evaluation

Evaluation Metrics:

R² Score
Mean Absolute Error (MAE)
Root Mean Squared Error (RMSE)
Cross Validation Score
🌐 Streamlit Application Features

✅ User-Friendly Interface

✅ Real-Time Delivery Time Prediction

✅ Interactive Input Fields

✅ Fast and Lightweight Deployment

Users can enter:

Distance
Weather
Traffic Level
Vehicle Type
Time of Day
Preparation Time
Courier Experience

and receive an estimated delivery time instantly.

📂 Project Structure
Food-Delivery-Time-Estimation/
│
├── app.py
├── Food_Delivery_Time_Estimation.ipynb
├── food_delivery_model.pkl
├── model_columns.pkl
├── Food_Delivery_Times.csv
├── requirements.txt
├── README.md
└── images/
🚀 Installation

Clone Repository:
git clone https://github.com/yourusername/Food_Delivery.git

Move to Project Folder:
cd Food_Delivery

Install Dependencies:
pip install -r requirements.txt

▶️ Run Streamlit App:
streamlit run app.py

Application will open at:

http://localhost:8501
📷 Sample Screenshots
Correlation Heatmap

Shows relationships between delivery factors and delivery time.

Delivery Time Distribution

Visualizes the distribution of target variable.

Feature Importance

Identifies the most influential factors affecting delivery time.

Streamlit Prediction Interface

Interactive application for real-time predictions.

📌 Key Insights
Distance is the most influential factor affecting delivery time.
Adverse weather conditions increase delivery duration.
High traffic significantly impacts delivery performance.
Courier experience helps reduce delivery delays.
Preparation time directly contributes to overall delivery time.
🎯 Future Enhancements
Deploy application on Streamlit Cloud
Integrate live traffic and weather APIs
Add delivery route optimization
Include advanced ensemble models
Build a Power BI dashboard for monitoring delivery KPIs
👨‍💻 Author

Sivanjaneya Banala

B.Tech Artificial Intelligence & Machine Learning (AIML)

Keshav Memorial Institute of Technology (KMIT)
