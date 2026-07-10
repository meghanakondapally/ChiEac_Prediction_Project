#  Chicago Education Prediction App

A machine learning web application that analyzes historical Chicago high school data and predicts key educational outcomes for selected schools.

##  Live Application

The project is deployed as an interactive Streamlit web application.

Users can select a Chicago high school and instantly view predicted educational outcomes.

##  Project Overview

This project uses multi-year Chicago education data to analyze school performance and build machine learning models for predicting:

- 🎓 Graduation Rate
- 🏫 College Enrollment Rate

The application allows users to select a school from an interactive dropdown. The system retrieves the school's latest available record and uses its school-level features as input to trained machine learning models.

## 🤖 Machine Learning Models

Two regression algorithms were evaluated:

| Model | Graduation MAE | Graduation RMSE | Graduation R² |
|---|---:|---:|---:|
| Linear Regression | 5.44 | 9.57 | 0.762 |
| Random Forest | 4.81 | 9.04 | 0.788 |

For college enrollment prediction:

| Model | MAE | RMSE | R² |
|---|---:|---:|---:|
| Linear Regression | 5.92 | 9.25 | 0.858 |
| Random Forest | 5.30 | 8.56 | 0.878 |

Random Forest achieved the best performance for both prediction tasks and was selected for deployment.

##  Application Workflow

1. User selects a Chicago high school.
2. The application retrieves the latest available school record.
3. Relevant school-level features are passed to the trained models.
4. The models generate predictions for:
   - Graduation rate
   - College enrollment rate
5. Results are displayed through the Streamlit interface.

##  Dataset

The project uses multi-year Chicago education data containing school-level information such as:

- Student enrollment
- Low-income student population
- Special education population
- English learners
- Student demographics
- School category
- Academic performance indicators
- Graduation rates
- College enrollment rates
- School year

> Note: This project makes predictions at the school level, not for individual students.

##  Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Random Forest Regression
- Linear Regression
- Joblib
- Streamlit
- GitHub
- Google Colab

##  Project Structure

    ChiEac_Prediction_Project/
    │
    ├── streamlit_app.py
    ├── app.py
    ├── requirements.txt
    │
    ├── data/
    │   ├── Chicago_Education_Master.csv
    │   ├── Chicago_Education_Cleaned.csv
    │   └── Chicago_High_School_Cleaned.csv
    │
    └── models/
        ├── graduation_rate_model.pkl
        └── college_enrollment_model.pkl

##  Run Locally

Clone the repository:

    git clone <your-repository-url>

Move into the project directory:

    cd ChiEac_Prediction_Project

Install dependencies:

    pip install -r requirements.txt

Run the Streamlit application:

    streamlit run streamlit_app.py

 Model Performance

Graduation Rate Prediction

The Random Forest model achieved:

- MAE: 4.81
- RMSE: 9.04
- R²: 0.788

This means the model explains approximately 78.8% of the observed variation in graduation rates within the evaluation dataset.

 College Enrollment Rate Prediction

The Random Forest model achieved:

- MAE: 5.30
- RMSE: 8.56
- R²: 0.878

This means the model explains approximately 87.8% of the observed variation in college enrollment rates within the evaluation dataset.

Limitations

- Predictions are made at the school level rather than the individual student level.
- Predictions depend on the quality and availability of historical data.
- Model outputs should be interpreted as analytical estimates rather than guaranteed future outcomes.
- Performance metrics are based on the project's evaluation split and may differ on unseen future data.
- The project should be reviewed for potential target leakage and temporal leakage before using predictions for real-world educational decisions.

 Future Improvements

Future versions could include:

- Historical performance trend charts
- Current vs predicted outcome comparisons
- At-risk school classification
- Feature importance visualization
- Model explainability using SHAP
- Geographic school maps
- Year-based forecasting
- Additional school performance indicators


**Meghana Kondapally**

Machine Learning and Data Analytics Project
