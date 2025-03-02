# -*- coding: utf-8 -*-
"""
@author:G
"""
import streamlit as st
import requests
import pandas as pd
import os
from datetime import datetime
from streamlit_js_eval import streamlit_js_eval  # For accurate geolocation

# File path for saving location data
file_path = "user_data.csv"

# Function to get user IP-based location (backup method)
def get_ip_location():
    try:
        response = requests.get("https://ipinfo.io/json")
        data = response.json()
        return data.get("city", "Unknown"), data.get("country", "Unknown"), data.get("ip", "Unknown")
    except:
        return "Unknown", "Unknown", "Unknown"

# Function to save data
def save_location_data(ip, city, country, lat, lon):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_entry = pd.DataFrame([[timestamp, ip, city, country, lat, lon]], 
                              columns=["Timestamp", "IP", "City", "Country", "Latitude", "Longitude"])

    if os.path.exists(file_path):
        new_entry.to_csv(file_path, mode='a', header=False, index=False)
    else:
        new_entry.to_csv(file_path, mode='w', index=False)

# Sidebar
st.sidebar.title("My Streamlit App")
st.title("Simple Addition App")

X = st.number_input("Enter value for X:", value=0.0, step=1.0)
Y = st.number_input("Enter value for Y:", value=0.0, step=1.0)

# Get accurate geolocation from browser
location = streamlit_js_eval(js_expressions="navigator.geolocation.getCurrentPosition((pos) => { return pos.coords.latitude + ',' + pos.coords.longitude; })")

if st.button("Calculate"):
    Z = X + Y
    st.success(f"Result: {Z}")

    # Get IP-based location
    city, country, ip = get_ip_location()

    if location:  # If browser location is available
        lat, lon = location.split(",")
    else:  # Otherwise, fallback to IP-based location
        lat, lon = "Unknown", "Unknown"

    # Save location data
    save_location_data(ip, city, country, lat, lon)

# Add a download button for CSV
if os.path.exists(file_path):
    with open(file_path, "rb") as file:
        st.download_button(
            label="📥 Download Location Data (CSV)",
            data=file,
            file_name="user_data.csv",
            mime="text/csv"
        )




    
    