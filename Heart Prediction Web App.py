# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 15:57:20 2023

@author: HP
"""

import numpy as np
import pickle
import streamlit as st

# loading the saved model
loaded_model = pickle.load(open('C:/Users/HP/Desktop/RECORDER/saved models/heart_disease_model.sav','rb'))

# Creating A Function For Prediction
def heart_disease_prediction (input_data):
    


    # change the input to numpy array
    data = np.array (input_data)

    # Reshape the numpy array because we are predicting for just one instance or data point
    input_data_reshaped = data.reshape(1, -1)


    prediction = loaded_model.predict (input_data_reshaped)
    print (prediction)


    if (prediction [0] == 0):
        return 'This Person Doesnt Have A Heart Disease'
    else:
        return'This Has A Heart Disease, See A Cardiologist'
        
        
def main ():
    
    # Givin A Title
    st.title ('Heart Disease Prediction Web App')
    
    # Getting Inputs From The User
    
    
    age = st.text_input('Age of Patient (age)')
    sex =st.text_input('Sex of Patient (sex)')
    cp = st.text_input('Chest Pain Type Value (cp)')
    trestbps = st.text_input('Resting Blood Pressure Value (trestbps)') 
    chol = st.text_input('CholesterolLevel (chol)')
    fbs = st.text_input('Fasting Blood Sugar (fbs)') 
    restecg = st.text_input('Resting Electrocardiographic Results (restecg)') 
    thalach = st.text_input('Maximum Heart Rate Achieved (thalach)')
    exang = st.text_input('Exercise-Induced Angina (exang)')
    oldpeak = st.text_input('ST Depression Induced by Exercise (oldpeak)')
    slope = st.text_input('Slope of the Peak Exercise ST Segment (slope)')
    ca = st.text_input('Number of Major Vessels Colored by Fluoroscopy (ca)')
    thal = st.text_input('Thallium Stress Test Result (thal)')
    
    
    # Code for Prediction
    diagnosis = ''
    
    # Creating A Button for Prediction
    
    if st.button ('Heart Disease Test Result'):
        diagnosis = heart_disease_prediction ([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
    
    st.success(diagnosis)
    
    
    
    
if __name__ == '__main__':
    main()
    

        