import joblib
import streamlit as st
import numpy as np

model = joblib.load("models/final_model.pkl")

st.title("🧠 Introvert vs Extrovert Classifier")
st.write("Answer the below questions to predict your personality type!")

with st.form(key='prediction form'):
    Time_spent_alone = st.slider("1. How much time do you spend alone daily? (0-10)", min_value=0, max_value=10)
    Stage_fear = st.radio("2. Do you have stage fear?", ["Yes", "No"])
    Social_event_attendance = st.slider("3. How often do you attend social events? (0-10)", min_value=0, max_value=10)
    Going_outside = st.slider("4. How often do you go outside per week? (0-10)", min_value=0, max_value=10)
    Drained_after_socializing = st.radio("5. Do you feel drained after socializing?", ["Yes", "No"])
    Friend_circle_size = st.slider("6. Number of friends in your circle. (0-20)", min_value=0, max_value=20)
    Post_frequency = st.slider("7. How often do you post on social media weekly? (0-10)", min_value=0, max_value=10)

    submitted = st.form_submit_button("Predict")


if submitted:
    # Encode categorical variables
    stage_fear = 1 if Stage_fear == "Yes" else 0
    drained = 1 if Drained_after_socializing == "Yes" else 0

    # Make prediction
    features = np.array([[Time_spent_alone, stage_fear, Social_event_attendance, Going_outside,
                          drained, Friend_circle_size, Post_frequency]])

    prediction = model.predict(features)

    if prediction == 1:
        st.success("✅ You're likely an **Extrovert**!")
    else:
        st.success("🧘 You're likely an **Introvert**.")
