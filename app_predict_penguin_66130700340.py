import streamlit as st
import pandas as pd
import pickle

# Load the trained model pipeline and encoders
try:
    with open('model_penguin_66130700340.pkl', 'rb') as file:
        model_pipeline, species_encoder = pickle.load(file)
    st.write("Model and encoders loaded successfully!")
except Exception as e:
    st.write("Error loading model and encoders:", e)

# Streamlit UI elements
st.title("Penguin Species Prediction")

# Input fields
island = st.selectbox("Island", ["Biscoe", "Dream", "Torgersen"])
culmen_length_mm = st.number_input("Culmen Length (mm)", min_value=0.0)
culmen_depth_mm = st.number_input("Culmen Depth (mm)", min_value=0.0)
flipper_length_mm = st.number_input("Flipper Length (mm)", min_value=0.0)
body_mass_g = st.number_input("Body Mass (g)", min_value=0.0)
sex = st.selectbox("Sex", ["MALE", "FEMALE"])

# Create a DataFrame for the input data
input_data = pd.DataFrame({
    'island': [island],
    'culmen_length_mm': [culmen_length_mm],
    'culmen_depth_mm': [culmen_depth_mm],
    'flipper_length_mm': [flipper_length_mm],
    'body_mass_g': [body_mass_g],
    'sex': [sex]
})

# Make predictions
try:
    prediction = model_pipeline.predict(input_data)
    predicted_species = species_encoder.inverse_transform(prediction)
    st.write("Predicted Species:", predicted_species[0])
except Exception as e:
    st.write("Error during prediction:", e)
