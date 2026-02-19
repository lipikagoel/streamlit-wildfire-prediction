import streamlit as st

st.title('California Wildfire Prediction App')

st.info('This is an app which if you input certain characteristics of weather, precipitation, locaiton, etc. it should display which areas within California are most at risk for wildfires')

with st.sidebar:
  st.header('Input features')
  location = st.selectbox
  date = st.date_input(value, format = "MM.DD.YYYY")
  
