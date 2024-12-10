import streamlit as st
import pandas as pd

# Title
st.title("Fertility Predictor")

# Load Data
data = pd.read_csv("fertility_data.csv")

# Inputs
age = st.slider("Select your age", 20, 40)
lifestyle = st.selectbox("Select your lifestyle", data['Lifestyle'].unique())

# Filter Data and Display Prediction
result = data[(data['Age'] == age) & (data['Lifestyle'] == lifestyle)]
if not result.empty:
    st.write(f"Fertility Score: {result['Fertility_Score'].values[0]}")
    st.write(f"Pregnancy Chance: {result['Pregnancy_Chance'].values[0]}")
else:
    st.write("No data available for this combination.")
