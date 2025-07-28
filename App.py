import streamlit as st
import pickle
import numpy as np

# Load model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Title
st.title("🎓 Student Performance Predictor")
st.write("Enter the following details:")

# Inputs
age = st.slider("Age", 15, 22, 17)
studytime = st.selectbox("Study Time", [1, 2, 3, 4])
failures = st.slider("Past Class Failures", 0, 4, 0)
absences = st.slider("Absences", 0, 30, 5)

sex = st.radio("Gender", ['Male', 'Female'])
sex = 1 if sex == 'Male' else 0

# Predict
if st.button("Predict"):
    input_data = np.array([[age, studytime, failures, absences, sex]])
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.success("✅ The student is likely to **PASS**.")
    else:
        st.error("❌ The student is likely to **FAIL**.")
