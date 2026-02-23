import streamlit as st
import requests
import plotly.express as px
import pandas as pd

API_URL = "https://app-wildfire-prediction-gvp5tpcymq2uae4qndccr9.streamlit.app/"

month_names = {
  1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8:"August", 9: "September", 10:"October", 11; "November", 12: "December"}

risk_assignment = {"Low": "#2ecc71", "Medium": "#f39c12", "High": "#e74c3c"}

st.set_page_config(page_title = "Cali Wild Risk", layout = "wide")

st.title('California Wildfire Prediction App')

st.info('This is an app which if you input certain characteristics of weather, precipitation, locaiton, etc. it should display which areas within California are most at risk for wildfires')
  
  
