import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
sns.set(style='dark')

##helper function
def create_daily_orders_df(df):
    daily_orders_df = df.resample(rule='M', on='dteday').agg({
        "casual": "sum",
        "registered" : "sum",
        "cnt": "sum"
    })
    daily_orders_df = daily_orders_df.reset_index()
    daily_orders_df.rename(columns={
        "casual": "total casual cust",
        "registered" : "total registered cust",
        "cnt" : "total cust"
    }, inplace=True)
    
    return daily_orders_df

def create_seasonal_orders_df(df):
    seasonal_orders_df = df.resample(rule='M', on='dteday').agg({
        "season" : "nunique",
        "casual": "sum",
        "registered" : "sum",
        "cnt": "sum"
    })
    seasonal_orders_df = seasonal_orders_df.reset_index()
    return seasonal_orders_df

## load data csv
df = pd.read_csv('day.csv')

## Order date
datetime_columns = ["dteday"]
df.sort_values(by="dteday", inplace=True)
df.reset_index(inplace=True)
for column in datetime_columns:
    df[column] = pd.to_datetime(df[column])

## Filter Component
min_date = df["dteday"].min()
max_date = df["dteday"].max()
with st.sidebar:
    
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu', min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

main_df = df[(df["dteday"] >= str(start_date)) & 
                (df["dteday"] <= str(end_date))]

## Memanggil helper function
daily_orders_df = create_daily_orders_df(main_df)
seasonal_orders_df = create_seasonal_orders_df(main_df)

## Dashoard
st.header('Bike Sharing Analysis Dashboard :sparkles:')

col1, col2 = st.columns(2)

with col1:
    total_orders = df.cnt.sum()
    st.metric("Total orders", value=total_orders)

with col2:
    total_revenue = df.cnt.count()
    st.metric("Total Revenue", value=total_revenue)

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    daily_orders_df["dteday"],
    daily_orders_df["total cust"],
    marker='o', 
    linewidth=2,
    color="#90CAF9"
)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
 
st.pyplot(fig)

fig, ax = plt.subplots(figsize=(16, 8))
sns.barplot(
        y="cnt", 
        x="season",
        data=seasonal_orders_df,
        ax=ax,
        errorbar=None
    )
st.pyplot(fig)
