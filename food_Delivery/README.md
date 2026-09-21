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
Clone Repository
git clone https://github.com/SivaBanala/Food-Delivery-Time-Estimation.git
Move to Project Folder:
cd Food-Delivery-Time-Estimation

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
