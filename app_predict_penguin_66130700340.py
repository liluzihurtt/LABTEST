import streamlit as st
import pandas as pd
import pickle
import sklearn.preprocessing
from sklearn.preprocessing import LabelEncoder

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


x_new =  pd.DataFrame() 
x_new['island'] = [island]
x_new['culmen_length_mm'] = [culmen_length_mm]
x_new['culmen_depth_mm'] = [culmen_depth_mm]
x_new['flipper_length_mm'] = [flipper_length_mm]
x_new['body_mass_g'] = [body_mass_g]
x_new['sex'] = [sex]

x_new['island'] = island_encoder.transform(x_new['island'])
x_new['sex'] = sex_encoder.transform(x_new['sex'])


# Make predictions
try:
    prediction = model_pipeline.predict(x_new)
    predicted_species = species_encoder.inverse_transform(prediction)
    st.write("Predicted Species:", predicted_species[0])
except Exception as e:
    st.write("Error during prediction:", e)
