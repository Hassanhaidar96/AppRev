# -*- coding: utf-8 -*-
"""
@author:G
"""
import streamlit as st
import requests

# Function to get user location
def get_location():
    try:
        response = requests.get("https://ipinfo.io/json")
        data = response.json()
        return data.get("city", "Unknown"), data.get("country", "Unknown"), data.get("ip", "Unknown")
    except Exception as e:
        return "Unknown", "Unknown", "Unknown"
    
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
    
    # Log the location
    st.write(f"Your Location: {city}, {country} (IP: {ip})")
    
    
    