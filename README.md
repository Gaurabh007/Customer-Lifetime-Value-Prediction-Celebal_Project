# 🧠 Customer Lifetime Value (CLV) Prediction Dashboard

A full-stack interactive Streamlit application that predicts the **future value of a customer** to a business using historical transaction data.

This project was developed as part of the **Celebal Internship Program** and uses machine learning and data-driven segmentation to classify customer types, predict repeat business in 3 and 6 months, and visualize their purchasing patterns.

---
## 🚀 Live Demo

🌐 **Streamlit App:** [Click Here to Launch](https://customervalueprediction.streamlit.app/)

---

## 🚀 Features

- 🧾 **Customer-Level CLV Prediction**
  - Predicts how much a customer is likely to spend in the next **3 and 6 months**
  - Built using **XGBoost Regression**

- 🔍 **Customer Type Detection**
  - Classifies customers as **Retail** or **Wholesaler** based on behavioral patterns

- 📊 **Interactive Dashboard**
  - Select a customer ID and instantly get:
    - CLV predictions
    - Country, customer type
    - Transaction history
    - Visualizations (monthly trends, product purchases, etc.)

- 📈 **Visual Analytics**
  - Product frequency bar charts
  - Monthly invoice trends
  - Customer type segmentation (Retail vs Wholesaler)

---

## 🛠️ Tech Stack

| Layer            | Tools Used                  |
|------------------|-----------------------------|
| **Frontend UI**  | Streamlit                   |
| **ML Model**     | XGBoost, scikit-learn       |
| **Data Wrangling** | Pandas, NumPy             |
| **Visualization** | Matplotlib, Seaborn        |
| **Deployment**   | Streamlit Cloud / Local     |

---

## 📂 Project Structure

customer-lifetime-value-prediction/<br>
├── app.py                      <br>
├── CLV_Prediction.ipynb        <br>
├── EDA.ipynb                   <br>
├── README.md                   <br>
├── requirements.txt            <br>
├──data/                       <br>
│&emsp; &emsp;├── online_retail_II.xlsx   <br>
│&emsp; &emsp;├── retail_cleaned_data.csv <br>
│&emsp; &emsp;└── features.csv            <br>
└── models/                     <br>
&emsp; &emsp;├── clv_model_3m.pkl        <br>
&emsp; &emsp;└── clv_model_6m.pkl        <br>



---

## 🧪 How It Works

1. **Data Cleaning:**  
   - Canceled transactions, missing CustomerIDs, and invalid records are removed

2. **Feature Engineering:**  
   - RFM metrics: Recency, Frequency, Monetary
   - Avg Unit Price, Avg Quantity
   - Segmentation into Retail/Wholesaler using heuristics

3. **Model Training:**  
   - CLV prediction model trained using past customer features
   - Labels created using a split between historic and recent months

4. **Dashboard & Inference:**  
   - User selects a `Customer ID`
   - Dashboard displays predictions, insights, and visuals

---

## 📊 Example Output

- **Customer 17850**
  - Country: United Kingdom
  - Type: 🏢 Wholesaler
  - Predicted Spend:
    - In 3 Months: £3450
    - In 6 Months: £5862

---
