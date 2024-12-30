# Sales Predictions for Bakery Item Categories

---

## Introduction

This project focuses on predicting sales for various bakery item categories, enabling improved inventory management, revenue forecasting, and resource allocation. It uses machine learning models, including SARIMA and Random Forest Regressor, to forecast sales and enhance decision-making processes.

Key objectives include:

- Predicting sales for the next week, month, and quarter/season.  
- Achieving a prediction confidence of **80-90%**.

Applications:

- **Inventory Management**  
- **Revenue Forecasting**  
- **Resource Allocation**  
- **Seasonal Planning**  

---

## Installation Instructions

1. Clone this repository:  
   ```bash
   git clone https://github.com/your-repository/sales-predictions.git
   ```
2. Navigate to the project directory:  
   ```bash
   cd sales-predictions
   ```
3. Install the required dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage Guide

1. Prepare the data by digitizing records from physical files.  
2. Preprocess the data (handle missing values, sort data, etc.).  
3. Train the models (SARIMA, Random Forest, etc.).  
4. Launch the Streamlit app for live predictions:  
   ```bash
   streamlit run app.py
   ```

---

## Results and Visuals

- **Model Performance:**  
  - Random Forest Regressor:  
    - Mean Squared Error (MSE): 11.174369  
    - R²: 0.13096  

- **Visuals:**  
  The Streamlit app includes interactive charts and seasonal trend visualizations for better decision-making.

---

## License Information

This project is licensed under the [MIT License](LICENSE).

