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
import joblib
import pandas as pd
import streamlit as st

st.set_page_config(page_title="CA Wildfire Risk Predictor", layout="wide")


@st.cache_resource
def load_assets():
    model = joblib.load("wildfire_model.pkl")
    encoder = joblib.load("fuel_encoder.pkl")
    features = joblib.load("feature_names.pkl")
    return model, encoder, features


model, le, feature_names = load_assets()

st.title("California Wildfire Prediction Dashboard")
st.markdown(
    "Enter environmental parameters to assess the probability of a wildfire event."
)

with st.sidebar:
    st.header("Input Parameters")

    lat = st.number_input("Latitude (32.5 - 42.0)", value=37.8)
    lon = st.number_input("Longitude (-124.4 - -114.1)", value=-122.4)
    hour = st.slider("Hour of Day (UTC)", 0, 23, 12)

    temp = st.slider("Avg Temperature (°C)", -10.0, 50.0, 25.0)
    precip = st.number_input("Precipitation (mm)", 0.0, 100.0, 0.0)
    wind = st.slider("Wind Speed (m/s)", 0.0, 40.0, 5.0)

    st.subheader("Land Characteristics")
    veg_cover = st.slider("Vegetation Cover (%)", 0, 100, 50)
    veg_height = st.slider("Vegetation Height (cm)", 0, 1000, 100)
    fuel_type = st.selectbox("Fuel Type", le.classes_)

if st.button("Predict Wildfire Risk"):
    fuel_encoded = le.transform([fuel_type])[0]

    input_data = pd.DataFrame(
        [[lat, lon, hour, temp, precip, wind, veg_cover, veg_height, fuel_encoded]],
        columns=feature_names,
    )

    prediction = model.predict(input_data)[0]
    prob = model.predict_proba(input_data)[0][1]

    st.divider()
    col1, col2 = st.columns(2)

    with col1:
        st.metric("Fire Risk Probability", f"{prob * 100:.1f}%")
        if prob > 0.7:
            st.error("⚠️ CRITICAL RISK LEVEL")
        elif prob > 0.4:
            st.warning("🟠 MODERATE RISK LEVEL")
        else:
            st.success("🟢 LOW RISK LEVEL")

    with col2:
        st.map(pd.DataFrame({"lat": [lat], "lon": [lon]}))
