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
import pandas as pd

## PAGE SETUP
st.set_page_config(page_title="TEST California Cities Map", layout = "wide")
st.header("California Wildfire Prediction")
st.markdown("Data from: Acquired from Meteostat, NASA Firms, LANDFIRE")


## SIDEBAR
with st.sidebar:
    st.title("Adjust the Risk Factors Here:") # sidebar title
    #fire = st.selectbox("Fire:",["A","B","C"]) # I don't think we need this, we just a user to input the data
    latitude = st.slider("Latitude", 32.5, 42.0,step = 0.01, format="%.2f") # slider selection
    longitude = st.slider("Longitutde", -124.4, 114.1,step = 0.01, format="%.2f") # slider selection
    acq_hour = st.slider("Acquired Hour:", 0, 23, 12)
    st.markdown("---")
    wx_tavg_c = st.number_input("Average Daily Temperature (C)", step=1, format="%d")
    wx_prcp_mm= st.number_input("Total Daily Precipitation (mL)",step = 0.01, format="%.2f")
    wx_wspd_ms= st.number_input("Wind Speed (m/s)",step = 0.01, format="%.2f")
    st.markdown("---")
    lf_evc= st.slider("Vegetation Cover (%)", 0, 100, 50)
    lf_evh= st.slider("Vegetation Height (cm)", 0, 1000, 100)
    # evt_fuel_n= st.selectbox("Fuel Type", le.classes_)
    #st.button("Apply Filters")

data = {
    "Latitude": [latitude],
    "Longitude": [longitude],
    "Hour in Day" : [acq_hour],
    "Avg Daily Temp (C)" : [wx_tavg_c],
    "Total Daily Prec (mL)" : [wx_prcp_mm],
    "Wind Speed (m/s)" : [wx_wspd_ms],
    "Veg Cover (%)" : [lf_evc],
    "Veg Height (cm)" : [lf_evh],
    # "Fuel Type" : [evt_fuel_n]
}

df = pd.DataFrame(data)
df = df.rename(index = {0: "Values:"})

df_bold = df.rename(columns={
    "Latitude": "**Latitude**",
    "Longitude": "**Longitude**",
    "Hour in Day" : "**Hour in Day**",
    "Average Daily Temp (C)" : "**Avg Daily Temp**",
    "Total Daily Prec (mL)" : "**Total Daily Prec**",
    "Wind Speed (m/s)" : "**Wind Speed**",
    "Veg Cover (%)" : "**Veg Cover**",
    "Veg Height (cm)" : "**Veg Height**",
}

st.dataframe(df.style.format("{:.2f}"), use_container_width=True) # for the table
