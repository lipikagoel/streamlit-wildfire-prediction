# California Wildfire Prediction App

An interactive **Streamlit web app** that lets users input weather-based conditions and visualize which areas of California are most at risk for wildfires — powered by a pre-trained machine learning model.

Built as a collaborative project for the **NSDC Winter 2026 Presentation**.

## Live Demo

[**App**](https://app-wildfire-prediction-gvp5tpcymq2uae4qndccr9.streamlit.app/)

## 📌 Features

- Input real-time or hypothetical weather parameters (temperature, humidity, wind speed, etc.)
- Predicts wildfire risk across California regions using a trained ML model
- Interactive map visualization highlighting at-risk areas
- Clean, user-friendly interface built with Streamlit

## Project Structure

```
streamlit-wildfire-prediction/
│
├── streamlit_app.py          # Main Streamlit application
├── wildfire_model.pkl        # Pre-trained wildfire prediction model
├── requirements.txt          # Python dependencies
│
├── Example/                  # Example test of making it
├── .streamlit/               # Streamlit configuration (theme, settings)
└── .gitignore
```

## Tech Stack

- **[Streamlit](https://streamlit.io/)** — web app framework
- **scikit-learn** — machine learning model (Random Forest)
- **pandas / numpy** — data processing
- **geopandas / folium / pydeck** — geospatial visualization *(update with what you're using)*
- **Python 3.x**

## 🚀 Getting Started

### 1. Clone the repository (with submodules)

```bash
git clone --recurse-submodules https://github.com/hsamala688/streamlit-wildfire-prediction.git
cd streamlit-wildfire-prediction
```

If you already cloned without submodules, run:

```bash
git submodule update --init --recursive
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
streamlit run streamlit_app.py
```

The app will open in your browser at `http://localhost:8501`.

## Deploy to Streamlit Cloud

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your repository and set the main file path to `streamlit_app.py`
4. Click **Deploy**

## Related Repository

The ML training pipeline lives in a separate repo:
👉 [CaliforniaWildfirePrediction](https://github.com/hsamala688/CaliforniaWildfirePrediction) — data engineering, model training, and evaluation notebooks

## Contributors

Built collaboratively as part of the **NSDC (National Student Data Corps) Winter 2026** project showcase.

Data Engineering Team:
- [Emiliano](https://github.com/emilianotorneltaki)
- [will](https://github.com/wllamjp)
- [arjun](https://github.com/ArjunBrahmandam)

Random Forest Team:
- [Aliya](https://github.com/aliyatang)
- [Joseph](https://github.com/Potato12fff)

[Streamlit App](https://app-wildfire-prediction-gvp5tpcymq2uae4qndccr9.streamlit.app/) Team:
- [Lipika](https://github.com/lipikagoel)
- [Hayden](https://github.com/hsamala688)

## License

This project is open source. Feel free to fork, use, and build upon it.
