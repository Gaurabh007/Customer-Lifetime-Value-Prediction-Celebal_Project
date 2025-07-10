import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import joblib

features = pd.read_csv("data/features.csv")  
df_full = pd.read_csv("data/retail_cleaned_data.csv") 
model_3m = joblib.load("models/clv_model_3m.pkl")
model_6m = joblib.load("models/clv_model_6m.pkl")


st.set_page_config(page_title="Customer CLV Dashboard", layout="wide")
st.title("🛍️ Customer Lifetime Value Prediction Dashboard")

# Sidebar - Customer Selector
customer_ids = sorted(features["Customer ID"].unique())
selected_id = st.sidebar.selectbox("Select a Customer ID", customer_ids)


cust_row = features[features["Customer ID"] == selected_id].squeeze()

X_input = cust_row[[
    "Recency", "Tenure", "Frequency", "TotalSpent",
    "TotalQuantity", "AvgUnitPrice", "AvgOrderValue", "AvgQuantity"
]].values.reshape(1, -1)

clv_3m = model_3m.predict(X_input)[0]
clv_6m = model_6m.predict(X_input)[0]

# Section 1: Predictions
st.subheader("📈 Future Value Prediction")
col1, col2, col3 = st.columns(3)

col1.metric("Predicted Spend in 3 Months", f"£{clv_3m:.2f}")
col2.metric("Predicted Spend in 6 Months", f"£{clv_6m:.2f}")
col3.metric("Customer Country", cust_row["Country"])

# Section 2: Past Purchase Summary
st.subheader("🧾 Past Purchase Summary")

col4, col5, col6, col7 = st.columns(4)
col4.metric("Recency (days)", int(cust_row["Recency"]))
col5.metric("Frequency (orders)", int(cust_row["Frequency"]))
col6.metric("Total Spent (£)", f"{cust_row['TotalSpent']:.2f}")
col7.metric("Avg Order Value (£)", f"{cust_row['AvgOrderValue']:.2f}")

# Section 3: Purchase History Table
st.subheader("🛒 Products Purchased")
cust_orders = df_full[df_full["Customer ID"] == selected_id]
product_summary = cust_orders.groupby("Description").agg({
    "Quantity": "sum",
    "TotalPrice": "sum"
}).reset_index().sort_values(by="TotalPrice", ascending=False)

st.dataframe(product_summary, use_container_width=True)

# ----------------------------------------------------Visualization----------------------------------------------------

st.subheader("📊 Purchase Behavior Visualizations")
col1, col2 = st.columns(2)



with col1:
# Monthly spend
    cust_orders["InvoiceMonth"] = pd.to_datetime(cust_orders["InvoiceDate"]).dt.to_period("M").astype(str)
    monthly_spending = cust_orders.groupby("InvoiceMonth")["TotalPrice"].sum()

    fig1, ax1 = plt.subplots(figsize=(5, 3))
    monthly_spending.plot(ax=ax1, marker='o', color='purple')
    ax1.set_title("Monthly Spending", fontsize=10)
    ax1.set_xlabel("Month", fontsize=8)
    ax1.set_ylabel("Spend (£)", fontsize=8)
    ax1.tick_params(axis='x', labelrotation=45, labelsize=7)
    ax1.tick_params(axis='y', labelsize=7)
    ax1.grid(True, linestyle='--', linewidth=0.5)

    # Top products
    top_products = cust_orders.groupby("Description")["TotalPrice"].sum().nlargest(10)
    fig2, ax2 = plt.subplots(figsize=(5, 3))
    top_products.plot(kind="barh", ax=ax2, color='darkgreen')
    ax2.set_title("Top Products", fontsize=10)
    ax2.set_xlabel("Spend (£)", fontsize=8)
    ax2.set_ylabel("Product", fontsize=8)
    ax2.tick_params(labelsize=7)
    ax2.invert_yaxis()

with col2:
# Scatter
    fig3, ax3 = plt.subplots(figsize=(5, 3))
    ax3.scatter(cust_orders["Price"], cust_orders["Quantity"], alpha=0.5, color='tomato', s=20)
    ax3.set_title("Quantity vs Price", fontsize=10)
    ax3.set_xlabel("Unit Price (£)", fontsize=8)
    ax3.set_ylabel("Quantity", fontsize=8)
    ax3.tick_params(labelsize=7)
    ax3.grid(True, linestyle='--', linewidth=0.5)

    # Monthly invoices
    invoice_counts = cust_orders.groupby("InvoiceMonth")["Invoice"].nunique()
    fig4, ax4 = plt.subplots(figsize=(5, 3))
    invoice_counts.plot(kind='bar', ax=ax4, color='steelblue')
    ax4.set_title("Invoices per Month", fontsize=10)
    ax4.set_xlabel("Month", fontsize=8)
    ax4.set_ylabel("Invoices", fontsize=8)
    ax4.tick_params(axis='x', labelrotation=45, labelsize=7)
    ax4.tick_params(axis='y', labelsize=7)


# --- Display Plots in 2x2 Grid ---
col3, col4 = st.columns(2)
with col3:
    st.pyplot(fig1)
with col4:
    st.pyplot(fig2)

col5, col6 = st.columns(2)
with col5:
    st.pyplot(fig3)
with col6:
    st.pyplot(fig4)



