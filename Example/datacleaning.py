import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

cols_to_use = [
    "fire",
    "latitude",
    "longitude",
    "acq_hour",
    "wx_tavg_c",
    "wx_prcp_mm",
    "wx_wspd_ms",
    "lf_evc",
    "lf_evh",
    "EVT_FUEL_N",
]

df = pd.read_csv("master_final.csv", usecols=cols_to_use)  # type: ignore


le = LabelEncoder()
if df is not None:
    df["fuel_type_encoded"] = le.fit_transform(df["EVT_FUEL_N"])  # pyright: ignore[reportOptionalMemberAccess]
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())

X = df.drop(columns=["fire", "EVT_FUEL_N"])
y = df["fire"]

model = RandomForestClassifier(
    n_estimators=100, max_depth=12, n_jobs=-1, random_state=42, class_weight="balanced"
)

model.fit(X, y)

joblib.dump(model, "wildfire_model.pkl")
joblib.dump(le, "fuel_encoder.pkl")
joblib.dump(X.columns.tolist(), "feature_names.pkl")
