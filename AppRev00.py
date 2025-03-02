# -*- coding: utf-8 -*-
"""
@author:G
"""
import streamlit as st
import requests
import pandas as pd
import os
from datetime import datetime

# Function to get user location
def get_location():
    try:
        response = requests.get("https://ipinfo.io/json")
        data = response.json()
        return data.get("city", "Unknown"), data.get("country", "Unknown"), data.get("ip", "Unknown")
    except Exception as e:
        return "Unknown", "Unknown", "Unknown"

# Function to save data to CSV
def save_location_data(ip, city, country):
    file_path = "user_data.csv"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Create DataFrame with new entry
    new_entry = pd.DataFrame([[timestamp, ip, city, country]], 
                              columns=["Timestamp", "IP", "City", "Country"])

    # Append to existing CSV or create new
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

    # Get user location
    city, country, ip = get_location()

    # Save to CSV (for analysis)
    save_location_data(ip, city, country)

    
    