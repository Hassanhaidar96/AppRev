# -*- coding: utf-8 -*-
"""
@author:G
"""
import streamlit as st
import requests
import pandas as pd
import os
from datetime import datetime

# File path to save data
file_path = "user_data.csv"

# Function to get user location
def get_location():
    try:
        response = requests.get("https://ipinfo.io/json")
        data = response.json()
        return data.get("city", "Unknown"), data.get("country", "Unknown"), data.get("ip", "Unknown")
    except:
        return "Unknown", "Unknown", "Unknown"

# Function to save data
def save_location_data(ip, city, country):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_entry = pd.DataFrame([[timestamp, ip, city, country]], 
                              columns=["Timestamp", "IP", "City", "Country"])

    if os.path.exists(file_path):
        new_entry.to_csv(file_path, mode='a', header=False, index=False)
    else:
        new_entry.to_csv(file_path, mode='w', index=False)

# Streamlit UI
st.sidebar.title("My Streamlit App")
st.title("Simple Addition App")

X = st.number_input("Enter value for X:", value=0.0, step=1.0)
Y = st.number_input("Enter value for Y:", value=0.0, step=1.0)

if st.button("Calculate"):
    Z = X + Y
    st.success(f"Result: {Z}")

    city, country, ip = get_location()
    save_location_data(ip, city, country)  # Save data

# Provide a download button to save the CSV file on local PC
if os.path.exists(file_path):
    with open(file_path, "rb") as file:
        st.download_button(label="Download User Data", data=file, file_name="user_data.csv", mime="text/csv")


    
    