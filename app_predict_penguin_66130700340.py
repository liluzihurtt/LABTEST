import pickle
import pandas as pd
import streamlit as st
from sklearn.preprocessing import LabelEncoder
 
with open('model_penguin_66130700340.pkl', 'rb') as file:
    # Only model_pipeline and species_encoder were saved
    model, species_encoder, island_encoder ,sex_encoder = pickle.load(file)
 
# Title of the app
st.title('Predict Randomforest Penguin App')
 
# Input fields for user to enter data
island = st.selectbox('Select island:', ['Torgersen', 'Biscoe', 'Dream'])
culmen_length_mm = st.number_input('Enter Culmen Length (mm):')
culmen_depth_mm = st.number_input('Enter Culmen Depth (mm):')
flipper_length_mm = st.number_input('Enter Flipper Length (mm):')
body_mass_g = st.number_input('Enter Body Mass (g):')
sex = st.selectbox('Select sex:', ['MALE', 'FEMALE'])
 
# Create a DataFrame from user input
x_new = pd.DataFrame()
x_new['island'] = [island]
x_new['culmen_length_mm']= [culmen_length_mm]
x_new['culmen_depth_mm']= [culmen_depth_mm]
x_new['flipper_length_mm']= [flipper_length_mm]
x_new['body_mass_g']= [body_mass_g]
x_new['sex']= [sex]
 
# Transform the input data using the encoders
x_new['island'] = island_encoder.transform(x_new['island'])
x_new['sex'] = sex_encoder.transform(x_new['sex'])
 
# Make predictions
y_pred_new = model.predict(x_new)
 
# Decode the predicted species
result = species_encoder.inverse_transform(y_pred_new)
 
# Display the prediction
st.write('Predicted Species:', result[0])
