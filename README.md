# 🎯 Marketing Campaign Conversion Predictor

An end-to-end Supervised Machine Learning project that predicts the likelihood of a customer **purchasing a product** based on their engagement metrics and demographic data.

## 🚀 Project Overview
This project addresses the challenge of optimizing marketing budgets by identifying "High-Intent" customers—those most likely to respond to a campaign offer. By utilizing an **XGBoost Classifier**, the model analyzes critical behavioral signals like page visits and discount sensitivity to predict conversion probability. This allows marketing teams to target their efforts precisely, increasing ROI and reducing wasted ad spend on "window shoppers."

## 🛠️ Tech Stack
* **Python:** Core language for data processing
* **XGBoost:** High-performance Gradient Boosting framework for classification
* **Scikit-Learn:** Machine Learning pipeline (StandardScaler, GridSearch, Evaluation)
* **Pandas & Seaborn:** Data Cleaning, Feature Engineering, and Exploratory Data Analysis (EDA)
* **Streamlit:** Web App Deployment for real-time lead scoring

## 📊 Key Features
* **Precision Targeting:** Identifies the specific segment of customers likely to convert, focusing on key drivers like **Product Page Visits** and **Discount Levels**.
* **Behavioral Analysis:** Distinguishes between passive browsing and active buying intent, helping marketers tailor their strategies (e.g., sending a coupon vs. a newsletter).
* **Manager-Friendly Interface:** The Streamlit web app allows marketing managers to input simple customer details and get an instant "Will Purchase / No Purchase" verdict with a confidence score.

## 🗺️ Project Pipeline
<img width="520" height="1441" alt="Marketing Project Flowchart" src="https://github.com/user-attachments/assets/aa7bb9b3-3b17-41cc-a072-ab52ca0e30e3" />

---

## 📈 Model Performance & Selection

### **1. Performance Summary**
* **Selected Model:** XGBoost Classifier
* **Accuracy:** **~89.2%** — High reliability in predicting customer conversion.
* **ROC-AUC Score:** **~0.82** — Strong ability to distinguish between high-intent buyers and casual browsers.
* **Precision (Class 1):** **~76%** — Effectively identifies true buyers, minimizing false positives (wasted marketing budget).

### **2. Why XGBoost?**
While **Logistic Regression** (~85%) and **Random Forest** (~87%) performed well, **XGBoost** was selected as the champion model because:
* **Gradient Boosting:** It builds trees sequentially, correcting the errors of previous trees, which makes it incredibly effective at capturing subtle patterns in user behavior.
* **Handling Mixed Data:** It excels at managing a mix of categorical (Gender) and continuous (Age, Page Visits) features without extensive preprocessing.
* **Feature Importance:** XGBoost provides clear insights into which factors (e.g., Discount Offered) actually drive the decision, making the model interpretable for business strategy.

---

## 🌐 Live Demo
Test the prediction system here:  
**[Marketing Campaign Conversion Predictor](https://marketing-campaign-conversion-predictor-aqyqjqmejbyqcu4dfkeauz.streamlit.app/)**

### 💤 Important Note on App Availability
If you are accessing the live demo and the website appears to be "sleeping":
* Please click the **"Yes, get this back up!"** button on the screen.
* This will wake up the server and restore the prediction tool within a few seconds.

---

## 🏁 How to Run Locally
1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR-USERNAME/marketing-campaign-conversion-predictor.git](https://github.com/YOUR-USERNAME/marketing-campaign-conversion-predictor.git)
