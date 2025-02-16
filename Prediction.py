import numpy as np
import pandas as pd
from PIL import Image
import streamlit as st
import pickle

# Load Model
lg = pickle.load(open('placement.pkl','rb'))

# Set Page Config
st.set_page_config(page_title="Career Hub Placement Prediction", page_icon="💼", layout="centered")

# Custom CSS for Dark Theme
st.markdown("""
    <style>
    body {
        background-color: black;
        color: yellow;
    }
    .stTextInput > div > div > input {
        background-color: #333;
        color: yellow;
    }
    .stButton > button {
        background-color: yellow;
        color: black;
        font-weight: bold;
    }
    .stButton > button:hover {
        background-color: black;
        color: yellow;
        border: 2px solid yellow;
    }
    .stTitle {
        color: yellow;
    }
    .stImage {
        border-radius: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# Load and Display Image
img = Image.open('doors-1690423.jpg')
st.image(img, width=650)

# Title
st.markdown("<h1 style='text-align: center;'>Career Hub Placement Prediction</h1>", unsafe_allow_html=True)

# Input Section
input_text = st.text_input("Enter All Features Here (comma-separated values):")

# Prediction Button
if st.button("Predict Placement"):
    if input_text:
        try:
            input_list = input_text.split(',')
            np_df = np.asarray(input_list, dtype=float)
            prediction = lg.predict(np_df.reshape(1, -1))
            
            if prediction[0] == 1:
                st.success("✅ This Person Is Placed!")
            else:
                st.error("❌ This Person Is Not Placed!")
        except ValueError:
            st.warning("⚠ Please enter valid numerical values separated by commas.")
    else:
        st.warning("⚠ Input field cannot be empty. Please enter feature values.")
