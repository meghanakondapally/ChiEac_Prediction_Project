import streamlit as st
import pandas as pd
import joblib

df = pd.read_csv("data/Chicago_High_School_Cleaned.csv")

grad_model = joblib.load("models/graduation_rate_model.pkl")
college_model = joblib.load("models/college_enrollment_model.pkl")

st.title("Chicago Education Prediction App")

school = st.selectbox("Select School", sorted(df["short_name"].dropna().unique()))

drop_cols = [
    "graduation_rate_school", "graduation_rate_mean",
    "college_enrollment_rate_school", "college_enrollment_rate_mean",
    "high_risk", "school_id", "short_name", "long_name",
    "website", "phone", "zip", "school_latitude", "school_longitude"
]

row = df[df["short_name"] == school].tail(1)
X = row.drop(columns=drop_cols, errors="ignore")

grad_pred = grad_model.predict(X)[0]
college_pred = college_model.predict(X)[0]

st.metric("Predicted Graduation Rate", f"{grad_pred:.2f}%")
st.metric("Predicted College Enrollment Rate", f"{college_pred:.2f}%")

st.subheader("School Data")
st.dataframe(row)
