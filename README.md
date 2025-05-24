Diabetes Prediction with Machine Learning and Django

This project predicts diabetes using various Machine Learning algorithms integrated into a Django web application.

Features

Algorithms Used:

Naive Bayes

Logistic Regression

Random Forest

K-Nearest Neighbors (KNN)

Support Vector Machine (SVM)

Decision Tree


Frontend: HTML, CSS, JavaScript

Backend: Django (Python)

Database: MySQL (can use SQLite for development)


How It Works

1. User inputs medical parameters (e.g., glucose, BMI, age, etc.).


2. Chooses an algorithm for prediction.


3. App uses pre-trained ML models to predict diabetes risk.


4. Result is displayed on the web interface.



Installation

git clone https://github.com/Muhammad051097/diabetes-prediction-ml.git
cd diabetes-prediction-ml
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
