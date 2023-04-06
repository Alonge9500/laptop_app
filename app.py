import streamlit as st 
import os
import joblib
import numpy as np
import pandas as pd
import json
    
RESOURCES_PATH = os.path.join(os.getcwd(), 'resources')
dictPath = os.path.join(RESOURCES_PATH,'propertydict.json')
modelPath = os.path.join(RESOURCES_PATH,'model.pkl')

model = joblib.load(modelPath)


with open(dictPath, 'r') as fp:
    propertydict = json.load(fp)
st.title('Flikpart Laptop')
st.header('Input your desire specifications to get an estimated price of your desire laptop')

with st.form('loan_form',clear_on_submit=True):
    ram_size = st.selectbox('Input Ram Size',propertydict[0].keys())
    ram_size = propertydict[0][ram_size]
    
    ram_type = st.selectbox('Input Ram Type',propertydict[1].keys())
    ram_type = propertydict[1][ram_type]
    
    processor = st.selectbox('Processor',propertydict[2].keys())
    processor = propertydict[2][processor]
    
    storage = st.selectbox('Storage',propertydict[3].keys())
    storage = propertydict[3][storage]
    
    storage_type = st.selectbox('Storage Type',propertydict[4].keys())
    storage_type = propertydict[4][storage_type]
    
    os_type = st.selectbox('OS',propertydict[5].values())
    propertydict[5] = {value: key for key, value in propertydict[5].items()}
    os_type = propertydict[5][os_type]
    
    display = st.selectbox('Display',propertydict[6].values())
    propertydict[6] = {value: key for key, value in propertydict[6].items()}
    display = propertydict[6][display]
    
    brand = st.selectbox('Brand',propertydict[7].values())
    propertydict[7] = {value: key for key, value in propertydict[7].items()}
    brand = propertydict[7][brand]
    
    
    features = np.array([ram_size,ram_type,processor,storage,storage_type,os_type,display,brand]).reshape(1,-1)
    submitted = st.form_submit_button()
    
    if submitted:
        prediction = round(np.exp(model.predict(features))[0])
        st.text(f'₹{prediction}')
