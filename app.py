import streamlit as st
import pandas as pd
import joblib
import numpy as np

# --- 1. LOAD MODEL AND ASSETS ---
try:
    model = joblib.load('mkt_conversion_pipeline.pkl')
    class_map = joblib.load('mkt_class_mapping.pkl')
except Exception as e:
    st.error(f"Error loading model files: {e}")
    st.info("Ensure 'mkt_conversion_pipeline.pkl' and 'mkt_class_mapping.pkl' are in the project folder.")

# --- 2. PAGE CONFIGURATION ---
st.set_page_config(page_title="Marketing Conversion AI", layout="centered")

st.title("🎯 Marketing Campaign Conversion Predictor")
st.write("Enter customer details below to predict purchase likelihood.")
st.divider()

# --- 3. UI LAYOUT ---
col1, col2 = st.columns(2)

with col1:
    age = st.slider("Age", 18, 90, 30)
    gender = st.selectbox("Gender", ["Male", "Female"])
    # We use a slider here to make interaction easier
    discount = st.slider("Discount Offered (%)", 0, 50, 10)

with col2:
    email_opened = st.number_input("Emails Opened", min_value=0, max_value=100, value=5)
    email_clicked = st.number_input("Emails Clicked", min_value=0, max_value=100, value=2)
    page_visits = st.number_input("Product Page Visits", min_value=0, max_value=100, value=3)

# --- 4. DATA PREPROCESSING ---
# Convert 'Gender' to numeric (1 for Male, 0 for Female)
gender_val = 1 if gender == "Male" else 0

# Create DataFrame with EXACT column names and order from training
feature_columns = [
    'Age', 
    'Gender', 
    'Email Opened', 
    'Email Clicked', 
    'Product page visit', 
    'Discount offered'
]

input_data = pd.DataFrame([[
    age, 
    gender_val, 
    email_opened, 
    email_clicked, 
    page_visits, 
    float(discount) # Ensure numeric consistency
]], columns=feature_columns)

# --- 5. PREDICTION LOGIC ---
if st.button("Analyze Conversion Probability", use_container_width=True):
    # Get Probability for Class 1 (Will Purchase)
    raw_prob = model.predict_proba(input_data)[0][1]
    
    # FIX: Convert float32 to standard Python float and clip to [0.0, 1.0]
    # This prevents the StreamlitAPIException
    probability = float(np.clip(raw_prob, 0.0, 1.0))
    
    # Get the binary prediction (0 or 1)
    prediction = int(model.predict(input_data)[0])
    
    # Display Results
    st.divider()
    m1, m2 = st.columns(2)
    
    with m1:
        st.metric("Conversion Probability", f"{probability:.2%}")
    
    with m2:
        result_label = class_map.get(prediction, "Unknown")
        if prediction == 1:
            st.success(f"Outcome: {result_label}")
        else:
            st.warning(f"Outcome: {result_label}")

    # Visual Progress Bar
    st.progress(probability)
    
    # Contextual Insight
    if probability > 0.7:
        st.info("💡 **Strategy:** This is a high-intent lead. Priority follow-up recommended.")
    elif probability > 0.4:
        st.info("💡 **Strategy:** Nurture this lead with additional personalized offers.")
    else:
        st.info("💡 **Strategy:** Low engagement. Focus on brand awareness rather than direct sales.")