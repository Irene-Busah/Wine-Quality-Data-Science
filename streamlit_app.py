# streamlit_app.py

import streamlit as st
import numpy as np
import os
import pandas as pd
from src.wine_quality.pipeline.prediction_pipeline import PredictionPipeline

st.set_page_config(page_title="Wine Quality Predictor", page_icon="🍷", layout="centered")

# Styling
st.markdown(
    """
    <style>
    .main { background-color: #f9f9f9; }
    .stButton>button {
        background-color: #800000;
        color: white;
        border-radius: 8px;
        padding: 10px 24px;
    }
    .stTextInput>div>div>input {
        border-radius: 6px;
    }
    </style>
    """, unsafe_allow_html=True
)

# Sidebar
st.sidebar.title("🍷 Wine Quality App")
page = st.sidebar.radio("Navigate", ["Predict Wine Quality", "Train Model", "About"])

# Prediction Page
if page == "Predict Wine Quality":
    st.title("🍇 Predict Wine Quality")

    if "predicted" not in st.session_state:
        st.session_state.predicted = False
    if "prediction_value" not in st.session_state:
        st.session_state.prediction_value = None

    if not st.session_state.predicted:
        st.markdown("Enter the features below to predict the quality of wine.")

        with st.form(key="predict_form"):
            fixed_acidity = st.number_input("Fixed Acidity", min_value=0.0, step=0.1)
            volatile_acidity = st.number_input("Volatile Acidity", min_value=0.0, step=0.01)
            citric_acid = st.number_input("Citric Acid", min_value=0.0, step=0.01)
            residual_sugar = st.number_input("Residual Sugar", min_value=0.0, step=0.1)
            chlorides = st.number_input("Chlorides", min_value=0.0, step=0.001)
            free_sulfur_dioxide = st.number_input("Free Sulfur Dioxide", min_value=0.0, step=1.0)
            total_sulfur_dioxide = st.number_input("Total Sulfur Dioxide", min_value=0.0, step=1.0)
            density = st.number_input("Density", min_value=0.0, step=0.0001)
            pH = st.number_input("pH", min_value=0.0, max_value=14.0, step=0.01)
            sulphates = st.number_input("Sulphates", min_value=0.0, step=0.01)
            alcohol = st.number_input("Alcohol", min_value=0.0, step=0.1)

            submit = st.form_submit_button("Predict Quality")

        if submit:
            try:
                # Create a DataFrame with proper column names
                input_df = pd.DataFrame([[
                    fixed_acidity, volatile_acidity, citric_acid, residual_sugar,
                    chlorides, free_sulfur_dioxide, total_sulfur_dioxide,
                    density, pH, sulphates, alcohol
                ]], columns=[
                    "fixed acidity", "volatile acidity", "citric acid", "residual sugar",
                    "chlorides", "free sulfur dioxide", "total sulfur dioxide",
                    "density", "pH", "sulphates", "alcohol"
                ])

                pipeline = PredictionPipeline()
                prediction = pipeline.predict(input_df)

                st.session_state.predicted = True
                st.session_state.prediction_value = prediction[0]

            except Exception as e:
                st.error(f"❌ Error during prediction: {e}")
    else:
        # Display result in a card style
        st.markdown("---")
        st.markdown("### 🍷 Prediction Result")
        st.markdown(
            f"""
            <div style="background-color: #fff4e6; padding: 25px; border-radius: 10px; border-left: 8px solid #800000;">
                <h2 style="color: #800000;">Wine Quality Score: <strong>{st.session_state.prediction_value}</strong></h2>
                <p style="font-size: 16px;">This is the predicted quality rating (0–10 scale) based on your inputs. 🍇</p>
                <p style="color: grey; font-size: 14px;">Note: Higher values suggest better quality wine.</p>
            </div>
            """, unsafe_allow_html=True
        )

        st.markdown("Would you like to try again?")
        if st.button("🔁 Predict Another Wine"):
            st.session_state.predicted = False
            st.session_state.prediction_value = None

# Train Page
elif page == "Train Model":
    st.title("⚙️ Train Model")
    st.markdown("Click the button below to retrain the model using `main.py`.")
    if st.button("Train Model"):
        with st.spinner("Training in progress..."):
            os.system("python main.py")
        st.success("✅ Model training completed successfully!")

# About Page
elif page == "About":
    st.title("ℹ️ About")
    st.markdown("""
    This application predicts wine quality based on physicochemical features.
    
    - Built with **Streamlit**
    - ML model powered by **scikit-learn** or your custom pipeline
    - Developed by [Your Name Here]
    """)
