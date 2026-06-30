import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Online Payment Fraud Detection",
    page_icon="💳",
    layout="wide"
)

model = joblib.load("fraud_detection_pipeline.pkl")
st.sidebar.title("About")

st.sidebar.info("""
This application predicts whether an online payment is fraudulent using a tuned Random Forest model trained on the PaySim dataset.
""")

st.title("💳 Online Payment Fraud Detection")

st.write(
    "Enter the transaction details below to predict whether the transaction is fraudulent."
)
amount = st.number_input("Amount", min_value=0.0)
oldbalanceOrg = st.number_input("Old Balance Origin", min_value=0.0)
newbalanceOrig = st.number_input("New Balance Origin", min_value=0.0)
oldbalanceDest = st.number_input("Old Balance Destination", min_value=0.0)
newbalanceDest = st.number_input("New Balance Destination", min_value=0.0)

day = st.number_input("Day", min_value=1, max_value=31)

hour = st.number_input("Hour", min_value=1, max_value=24)

transaction_type = st.selectbox(
    "Transaction Type",
    [
        "CASH_IN",
        "CASH_OUT",
        "DEBIT",
        "PAYMENT",
        "TRANSFER"
    ]
)

if st.button("Predict Fraud"):

    input_df = pd.DataFrame({

        "amount":[amount],
        "oldbalanceOrg":[oldbalanceOrg],
        "newbalanceOrig":[newbalanceOrig],
        "oldbalanceDest":[oldbalanceDest],
        "newbalanceDest":[newbalanceDest],
        "day":[day],
        "hour":[hour],
        "type":[transaction_type]

    })

    prediction = model.predict(input_df)[0]

    probability = model.predict_proba(input_df)[0][1]

    if prediction == 1:
        st.error(f"⚠ Fraud Detected\n\nProbability: {probability:.2%}")
    else:
        st.success(f"✅ Legitimate Transaction\n\nProbability of Fraud: {probability:.2%}")