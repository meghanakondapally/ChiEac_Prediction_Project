import gradio as gr
import pandas as pd
import joblib

df = pd.read_csv("data/Chicago_High_School_Cleaned.csv")

grad_model = joblib.load("models/graduation_rate_model.pkl")
college_model = joblib.load("models/college_enrollment_model.pkl")

schools = sorted(df["short_name"].dropna().unique())

drop_cols = [
    "graduation_rate_school",
    "graduation_rate_mean",
    "college_enrollment_rate_school",
    "college_enrollment_rate_mean",
    "high_risk",
    "school_id",
    "short_name",
    "long_name",
    "website",
    "phone",
    "zip",
    "school_latitude",
    "school_longitude"
]

def predict_school(school):
    row = df[df["short_name"] == school].tail(1)
    X = row.drop(columns=drop_cols, errors="ignore")

    grad_pred = grad_model.predict(X)[0]
    college_pred = college_model.predict(X)[0]

    return f"{grad_pred:.2f}%", f"{college_pred:.2f}%"

app = gr.Interface(
    fn=predict_school,
    inputs=gr.Dropdown(schools, label="Select School"),
    outputs=[
        gr.Textbox(label="Predicted Graduation Rate"),
        gr.Textbox(label="Predicted College Enrollment Rate")
    ],
    title="Chicago Education Prediction App"
)

app.launch(server_name="0.0.0.0", server_port=7860)
