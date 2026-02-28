import streamlit as st
import pandas as pd
import numpy as np

## PAGE SETUP
st.set_page_config(page_title="TEST California Cities Map", layout = "wide")
st.title("California Wildfire Prediction", anchor = "main title")

url1 = "https://data.ca.gov/dataset/climate-land-cover-landfire-derived"
url2 = "https://meteostat.net/en/"
url3 = "https://firms.modaps.eosdis.nasa.gov/map/#d:24hrs;@0.0,0.0,3.0z"
url4 = "https://github.com/hsamala688/CaliforniaWildfirePrediction"

st.write("Data from: Acquired from [California Landfire](%s)" % url1, ", [Meteostat](%s)" % url2, ", [NASA FIRMS](%s)" % url3)
st.markdown("Predictions Made Through a [Random Forest Classifier Model](%s)" % url4)


st.markdown("---")

def reset():
    for key in st.session_state.keys():
        del st.session_state[key]
    st.rerun()

## SIDEBAR
with st.sidebar:
    st.title("Adjust the Risk Factors:") # sidebar title
    #fire = st.selectbox("Fire:",["A","B","C"]) # I don't think we need this, we just a user to input the data
    
    latitude = st.slider("Latitude", 
                         32.5, 42.0,
                         step = 0.01, 
                         format="%.2f", 
                         value=st.session_state.get("lat_input",34.0689),
                         key = "lat_input") # changed these so that they only have 2 decimal points
    
    longitude = st.slider("Longitutde", 
                          -124.4, -114.1,
                          step = 0.01, 
                          format="%.2f", 
                          value=st.session_state.get("lon_input",-118.4452),
                          key = "lon_input") # changed these so that they only have 2 decimal points
    
    acq_hour = st.slider("Acquired Hour:", 
                         0, 23, 
                         value = st.session_state.get("hour_input", 12), 
                         key = "hour_input")
    
    st.markdown("---")
    
    wx_tavg_c = st.number_input("Average Daily Temperature (C)", 
                                step=1, format="%d", 
                                value = st.session_state.get("temp_input", 12), 
                                key = "temp_input")
    
    wx_prcp_mm= st.number_input("Total Daily Precipitation (mm)",
                                step = 0.01, 
                                format="%.2f", 
                                value = st.session_state.get("prec_input", 0.0),
                                key = "prec_input") # changed these so that they only have 2 decimal points
    
    wx_wspd_ms= st.number_input("Wind Speed (m/s)", 
                                step = 0.01, 
                                format="%.2f", 
                                value = st.session_state.get("wind_input", 0.0),
                                key = "wind_input") # changed these so that they only have 2 decimal points
    
    st.markdown("---")
    lf_evc= st.slider("Vegetation Cover (%)", 
                      0, 100, 50, 
                      value = st.session_state.get("veg_cov_input", 0),
                      key = "veg_cov_input")
    
    lf_evh= st.slider("Vegetation Height (cm)", 
                      0, 1000, 100, 
                      value = st.session_state.get("veg_hei_input", 0),
                      key = "veg_hei_input")
    
    # evt_fuel_n= st.selectbox("Fuel Type", le.classes_)

col_btn1, col_btn2 = st.columns(2)

with col_btn1:
    clicked = st.button("Predict", type = "primary", use_container_width = "True")

with col_btn2:
    if st.button("Clear Values", use_container_width=True):
        reset()
    
st.subheader("Specific Location Risk Assessment:")

# DataFrame Setup
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

st.dataframe(df.style.format("{:.2f}"), use_container_width=True) # for the table

st.map(pd.DataFrame({"lat": [latitude], "lon": [longitude]}))

# setting up the logic for whats supposed to happen with the button press
#if the button Predict Wildfire Risk is pressed runs the joblib files, then for that specific point what is the risk. Can't do that without model
# Creating a map so shows state-wide risk given certain conditions

st.markdown("---")

# Second Dataframe Setup

data2 = {
    "Hour in Day" : [acq_hour],
    "Avg Daily Temp (C)" : [wx_tavg_c],
    "Total Daily Prec (mL)" : [wx_prcp_mm],
    "Wind Speed (m/s)" : [wx_wspd_ms],
    "Veg Cover (%)" : [lf_evc],
    "Veg Height (cm)" : [lf_evh],
}

df2 = pd.DataFrame(data2)

df2 = df2.rename(index = {0: "Values:"})

st.dataframe(df2.style.format("{:.2f}"), use_container_width=True)

st.subheader("Overall State Risk Assessment:")

if st.button("Generate Statewide Heatmap", use_container_width=True):
    with st.spinner("Processing..."):
        lats = np.linspace(32.5, 42.0)
        longs = np.linspace(-124.4, -114.1)
        grid_points = [(lats,longs) for lat in lats for lon in longs]
        grid_df = pd.DataFrame(grid_points, columns=['latitude', 'longitude'])
    
        grid_df[acq_hour] = acq_hour
        grid_df[wx_tavg_c] = wx_tavg_c
        grid_df[wx_prcp_mm] = wx_prcp_mm
        grid_df[wx_wspd_ms] = wx_wspd_ms
        grid_df[lf_evc] = lf_evc
        grid_df[lf_evh] = lf_evh

        # Now still waiting for model once it is trained we can add the final part to this code
        # this parts goal is that taking the same model use it to predict overall state risk and create a map
        
        
