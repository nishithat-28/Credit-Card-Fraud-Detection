# 💳 Credit Card Fraud Detection
<br>
## 📝 Overview
This project implements a machine learning model to detect fraudulent transactions in credit card datasets. It uses various Decision Tree as the classification algorithms to identify anomalies and distinguish between legitimate and fraudulent transactions.

<br>
## ✨ Features
- 🔍 **Data Preprocessing**: Clean and prepare data for analysis.
- 📊 **Exploratory Data Analysis (EDA)**: Visualize and understand the dataset.
- 🤖 **Machine Learning Models**: Decision Tree, KNN, Logistic Regression, SVM
- 📈 **Evaluation Metrics**: Accuracy, Precision, Recall, F1-score, and AUC-ROC.
- 🌐 **Deployment**: Web application built with Flask, HTML and CSS.
- 🚀 **Run the Application**:  
  Launch the app using the following command:
  ```bash
  python app.py
  ```
  <br>
  Access the web app at `http://localhost:5000`.

<br>
## 📂 Dataset
The dataset contains transactions made by credit cards, including both fraudulent and legitimate transactions.   
This dataset presents transactions that occurred in two days, where we have 492 frauds out of 284,807 transactions. The dataset is highly unbalanced, the positive class (frauds) account for 0.172% of all transactions.    <br><br>
Download the dataset from [Kaggle](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud).  
<br>
- **Attributes**: 
  -  `Time`: Seconds elapsed between this transaction and the first transaction.
  -  `V1-V28`: Principal components obtained from PCA.
  -  `Amount`: Transaction amount.
  -  `Class`: Target variable (0 for legitimate, 1 for fraudulent). 

<br>
## 📊 Model Performance
- Accuracy: 99.9%
- Precision: 75%
- Recall: 81%
- F1-Score: 78% 

<br>
## 🛠️ Requirements
-  Python 3.x
-  Libraries: 
  - `numpy`
  - `pandas`
  - `matplotlib`
  - `seaborn`
  - `scikit-learn`
  - `flask`
  - `pickle` or `joblib`

---

