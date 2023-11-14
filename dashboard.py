import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
sns.set(style='dark')

df = pd.read_csv('day.csv')

st.title('Dashboard Analisis Data Bike Sharing')

col1, col2 = st.columns(2)

with col1:
    total_orders = df.cnt.sum()
    st.metric("Total orders", value=total_orders)

with col2:
    total_revenue = df.cnt.count()
    st.metric("Total Revenue", value=total_revenue)

# tab1, tab2= st.tabs(["Tab 1", "Tab 2"])
 
# with tab1:
#     st.header("Reports")

#     st.subheader('Daily Orders')

#     col1, col2 = st.columns(2)

#     with col1:
#         total_orders = daily_orders_df.order_count.sum()
#         st.metric("Total orders", value=total_orders)
    
#     with col2:
#         total_revenue = format_currency(daily_orders_df.revenue.sum(), "AUD", locale='es_CO') 
#         st.metric("Total Revenue", value=total_revenue)
        
#     with st.container():
#         st.write("Inside the container")
        
#         x = np.random.normal(15, 5, 250)
    
#         fig, ax = plt.subplots()
#         ax.hist(x=x, bins=15)
#         st.pyplot(fig) 
# with tab2:
#     st.header("Monthly")
#     with st.container():
#         st.write("Inside the container")
        
#         x = np.random.normal(15, 5, 250)
    
#         fig, ax = plt.subplots()
#         ax.hist(x=x, bins=15)
#         st.pyplot(fig) 