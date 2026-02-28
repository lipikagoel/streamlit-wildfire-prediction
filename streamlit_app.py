"""
Hey, here are you instructions for what I want the streamlit page to have. I would like the page to have a fairly
simply UI, but feel free to customize as you go along.

Add a sidebar where a user can input information for the following fields:
'fire', 'latitude', 'longitude', 'acq_hour', 'wx_tavg_c', 'wx_prcp_mm', 'wx_wspd_ms', 'lf_evc', 'lf_evh', 'EVT_FUEL_N'

Consider this list as a temporary placeholder as the ML team decides what columns they are going to be using for the RCF
model.

If you need any help please refer to the folder labeled Example which houses an example streamlit script as well as
the associated RCF model as well as the requisite PKL files needed for the model to work.

Let me know within the next couple days how far you get and feel free to delete this block of comments once you are
done

Also for you to be able to deploy the app itself feel free to fork the repository and test it out on your own.
"""

import streamlit as st
import datetime

## PAGE SETUP
st.set_page_config(page_title="TEST California Cities Map")
st.subheader("California Wildfire Prediction")
st.markdown("Data from: `...`.")

## SIDEBAR
with st.sidebar:
    st.title("Risk Factors") # sidebar title
    fire = st.selectbox("Fire:",["A","B","C"]) # dropdown selection
    latitude = st.slider("Latitude", -90, 90) # slider selection
    latitude = st.slider("Longitutde", -90, 90) # slider selection
    acq_hour = st.time_input("Acquired Hour:", "12:00")
    wx_tavg_c = st.number_input("Average Daily Temperature (C)", step=1, format="%d")
    wx_prcp_mm= st.number_input("Total Daily Precipitation (mL)")
    wx_wspd_ms= st.number_input("Wind Speed (m/s)")
    lf_evc= st.number_input("Density of Vegetation")
    lf_evh= st.selectbox("Amount of Vegetation", ["Low", "High"])
    evt_fuel_n= st.selectbox("Fuel Identifier", ["Option 1", "Option 2"])
    st.markdown("---") # Add a horizontal rule
    st.button("Apply Filters")

# st.write(f"You selected: {fire} and {latitude}") # write what options have been selected (onto main page)

# selected_page = st.sidebar.radio('Go to', ['Page 1', 'Page 2', 'Page 3']) # single-select multiple choice

# st.sidebar.header('Filters')

# date_range = st.sidebar.date_input('Select Date Range')
