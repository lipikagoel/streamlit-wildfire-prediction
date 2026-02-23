import pandas as pd
import plotly.express as px
import requests
import streamlit as st

API_URL = "http://localhost:8000/predict"

MONTH_NAMES = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}

RISK_COLORS = {"Low": "#2ecc71", "Medium": "#f39c12", "High": "#e74c3c"}

st.set_page_config(page_title="California Wildfire Risk", layout="wide")

st.title("California Wildfire Risk Predictor")
st.markdown(
    "Select a month to see predicted wildfire risk levels across all 58 California counties."
)

# Month selector
selected_month = st.selectbox(
    "Select Month",
    options=list(MONTH_NAMES.keys()),
    format_func=lambda x: MONTH_NAMES[x],
    index=6,  # Default to July (high risk season)
)

if st.button("Predict Risk", type="primary"):
    with st.spinner(f"Getting predictions for {MONTH_NAMES[selected_month]}..."):
        try:
            response = requests.post(
                API_URL, json={"month": selected_month}, timeout=10
            )
            response.raise_for_status()
            data = response.json()

            df = pd.DataFrame(data["predictions"])

            risk_order = {"Low": 0, "Medium": 1, "High": 2}
            df["risk_numeric"] = df["risk"].map(lambda x: risk_order.get(x))

            fig = px.choropleth(
                df,
                geojson="https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json",
                locations="fips",
                color="risk",
                color_discrete_map=RISK_COLORS,
                category_orders={"risk": ["Low", "Medium", "High"]},
                scope="usa",
                hover_name="county",
                hover_data={"fips": False, "risk": True},
                title=f"Wildfire Risk Predictions — {MONTH_NAMES[selected_month]}",
                labels={"risk": "Risk Level"},
            )

            fig.update_geos(fitbounds="locations", visible=False)

            fig.update_layout(
                margin={"r": 0, "t": 40, "l": 0, "b": 0},
                height=600,
                legend_title_text="Risk Level",
            )

            st.plotly_chart(fig, use_container_width=True)

            # --- Summary stats below the map ---
            st.markdown("### County Breakdown")
            col1, col2, col3 = st.columns(3)

            for risk, color, col in zip(
                ["High", "Medium", "Low"],
                ["#e74c3c", "#f39c12", "#2ecc71"],
                [col1, col2, col3],
            ):
                counties_at_risk = df[df["risk"] == risk]["county"].tolist()
                with col:
                    st.markdown(
                        f"**:{color.replace('#', '')} {risk} Risk ({len(counties_at_risk)} counties)**"
                    )
                    st.markdown(
                        ", ".join(sorted(counties_at_risk))
                        if counties_at_risk
                        else "None"
                    )

        except requests.exceptions.ConnectionError:
            st.error(
                "Could not connect to the prediction API. Make sure the FastAPI server is running at "
                + API_URL
            )
        except requests.exceptions.HTTPError as e:
            st.error(f"API error: {e}")
        except Exception as e:
            st.error(f"Something went wrong: {e}")

st.markdown("---")
st.caption(
    "Proof of concept — predictions based on synthetic historical data. Real model coming soon."
)
