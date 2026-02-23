import streamlit as st
import requests
import plotly.express as px
import pandas as pd


st.title('California Wildfire Prediction App')

st.info('This is an app which if you input certain characteristics of weather, precipitation, locaiton, etc. it should display which areas within California are most at risk for wildfires')

with st.sidebar:
  st.header('Input features')
  #
  date = st.date_input("Enter the Date:", min_value=date(2020, 1, 1), max_value=date(2025, 12, 31))
  
  
