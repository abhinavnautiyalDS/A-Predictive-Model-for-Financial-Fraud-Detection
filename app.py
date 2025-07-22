import streamlit as st
import pandas as pd
import joblib
from datetime import datetime
import base64

# === Page Configuration ===
st.set_page_config(page_title="💳 Fraud Detection App", layout="centered")

# Encode the background image in base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

encoded_bg = get_base64_image('6367395.jpg')  # replace with your image file path

# Inject Custom CSS for styling
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded_bg}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    h1, h2, h3, h4, h5, h6, .stMarkdown {{
        font-size: 24px !important;
        color: white !important;
        text-shadow: 1px 1px 3px black;
    }}

    label, .css-1d391kg p, .css-1v0mbdj p, .css-1v0mbdj {{
        font-size: 18px !important;
        color: white !important;
        text-shadow: 1px 1px 3px black;
    }}

    .stButton>button {{
        background-color: #0072B2;
        color: white;
        font-size: 18px;
        border-radius: 8px;
        padding: 0.5em 1.5em;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# === Load model and features ===
model = joblib.load('fraud_detection_model.pkl')
model_features = joblib.load('model_features.pkl')

# === Title ===
st.title("💳 Fraud Detection Prediction")

st.markdown("Enter the **transaction details** below 👇")

# === User Inputs ===
transaction_type = st.selectbox("Transaction Type", ['TRANSFER', 'CASH_OUT', 'PAYMENT', 'DEBIT', 'CASH_IN'])
amount = st.number_input("Transaction Amount", min_value=0.0, step=0.01)
oldbalanceOrg = st.number_input("Origin Account Balance", min_value=0.0, step=0.01)
current_hour = st.number_input("Transaction Hour of Day (0-23)", min_value=0, max_value=23, value=datetime.now().hour)

# === Backend Calculations ===
newbalanceOrig = max(oldbalanceOrg - amount, 0)
org_balance_change = oldbalanceOrg - newbalanceOrig
amount_to_balance_ratio = round(amount / (oldbalanceOrg + 1), 2)
flag_org_balance_change = 1 if org_balance_change == amount else 0
flag_amount_to_balance_ratio = 1 if amount_to_balance_ratio >= 0.9 else 0

def categorize_hour(hour):
    if 5 <= hour < 12:
        return 'Morning'
    elif 12 <= hour < 17:
        return 'Afternoon'
    elif 17 <= hour < 21:
        return 'Evening'
    else:
        return 'Night'

hour_category = categorize_hour(current_hour)

# === Prepare input dataframe ===
input_data = pd.DataFrame({
    'type': [transaction_type],
    'amount': [amount],
    'oldbalanceOrg': [oldbalanceOrg],
    'newbalanceOrig': [newbalanceOrig],
    'org_balance_change': [org_balance_change],
    'AmountToBalanceRatio_Orig': [amount_to_balance_ratio],
    'flag_org_balance_change': [flag_org_balance_change],
    'flag_AmountToBalanceRatio_Orig': [flag_amount_to_balance_ratio],
    'Hour_of_day': [current_hour],
    'Hour_Category': [hour_category]
})

input_data = pd.get_dummies(input_data)

# Ensure all required features are present
for col in model_features:
    if col not in input_data.columns:
        input_data[col] = 0

input_data = input_data[model_features]

# === Prediction Button ===
if st.button("🔎 Predict Fraud"):
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    if prediction == 1:
        st.error(f"⚠️ This transaction is likely **FRAUDULENT** with a probability of **{probability:.2%}**.")
    else:
        st.success(f"✅ This transaction is likely **SAFE**, with a fraud probability of **{probability:.2%}**.")
