import joblib
import streamlit as st
import numpy as np
import pandas as pd
import shap
import matplotlib.pyplot as plt
import os

# Load model
model = joblib.load("C:/Users/HUB/Desktop/extrovert_vs_introvert/models/final_model.pkl")

# Set up SHAP Explainer
explainer = shap.Explainer(model)

st.title("🧠 Introvert vs Extrovert Classifier")
st.write("Answer the below questions to predict your personality type!")

with st.form(key='prediction_form'):
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

    feature_names = ["Time_spent_alone", "Stage_fear", "Social_event_attendance", "Going_outside",
                          "Drained_after_socializing", "Friend_circle_size", "Post_frequency"]

    input_df = pd.DataFrame(features, columns=feature_names)

    prediction = model.predict(features)[0]

    prediction_label = "Extrovert" if prediction == 1 else "Introvert"
    st.success(f"✅ You're likely an **{prediction_label}**.")

    class_index = prediction
    # Get the shap_values object
    shap_values = explainer(input_df)

    st.session_state.inputs = {
            "Time_spent_alone": Time_spent_alone,
            "Stage_fear": stage_fear,
            "Social_event_attendance": Social_event_attendance,
            "Going_outside": Going_outside,
            "Drained_after_socializing": drained,
            "Friend_circle_size": Friend_circle_size,
            "Post_frequency": Post_frequency,
            "Prediction": prediction_label,
        }


    # Extract only the values for the predicted class (class_index)
    shap_value = shap.Explanation(
        values=shap_values.values[0, class_index],
        base_values=shap_values.base_values[0, class_index],
        data=shap_values.data[0],
        feature_names=shap_values.feature_names
    )

    # Plot and render
    st.subheader("🔍 Why this prediction?")
    fig, ax = plt.subplots(figsize=(10, 4))
    shap.plots.waterfall(shap_value, show=False)
    st.pyplot(fig)

# Setting feedback loop
if "inputs" in st.session_state:
    st.markdown("---")
    feedback = st.radio("🧠 Was this prediction accurate?", ["Yes", "No"])
    if st.button("Submit Feedback"):

        feedback_data = st.session_state.inputs.copy()
        feedback_data["Feedback"] = feedback

        feedback_df = pd.DataFrame([feedback_data])

        if os.path.exists("feedback.csv"):
            feedback_df.to_csv("feedback.csv", mode="a", header=False, index=False)
        else:
            feedback_df.to_csv("feedback.csv", index=False)
        st.success("✅ Thank you! Your feedback was recorded.")