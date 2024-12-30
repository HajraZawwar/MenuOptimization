import streamlit as st
import pandas as pd
import pickle
import os
from statsmodels.tsa.statespace.sarimax import SARIMAXResults

# Directory where models are saved
model_dir = "./sarima_models"

st.set_page_config(page_title="SARIMA Model Prediction App", layout="wide")

# Load available models
models = {}
for file in os.listdir(model_dir):
    if file.endswith(".pkl"):
        category = file.split("_")[-1].replace(".pkl", "")
        with open(os.path.join(model_dir, file), 'rb') as f:
            models[category] = pickle.load(f)

print("models_loaded")

st.title("Sales Forcasting | SARIMA Model")

# User selects category
categories = list(models.keys())
selected_category = st.selectbox("Select a Category", categories)

if selected_category:
    st.write(f"Selected Category: {selected_category}")
    
    # Load the corresponding model
    model = models[selected_category]
    
    # User inputs prediction steps
    forecast_steps = st.number_input(
        "Enter the number of days to forecast", 
        min_value=1, 
        max_value=365, 
        value=30
    )
    
    if st.button("Generate Forecast"):
        # Generate forecast
        forecast = model.get_forecast(steps=forecast_steps)
        forecast_mean = forecast.predicted_mean
        forecast_conf_int = forecast.conf_int()
        
        # Display forecast results
        st.subheader("Forecast Results")
        start_date = pd.Timestamp("2024-11-08")
        forecast_df = pd.DataFrame({
            "Date": pd.date_range(start=start_date, periods=forecast_steps, freq="D"),
            "Forecast": forecast_mean,
            "Lower Bound": forecast_conf_int.iloc[:, 0],
            "Upper Bound": forecast_conf_int.iloc[:, 1]
        })
        forecast_df.set_index("Date", inplace=True)
        st.dataframe(forecast_df, use_container_width=True)

        # Plot the forecast
        st.subheader("Forecast Plot")
        st.line_chart(forecast_df[["Forecast", "Lower Bound", "Upper Bound"]])
