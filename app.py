import streamlit as st # type: ignore
import pandas as pd # type: ignore
import plotly.express as px # type: ignore

# Ensure the dataset path is relative to the root directory.
df = pd.read_csv('vehicles_us.csv')

st.header("My Data Dashboard")

# Example of adding a chart
fig = px.histogram(df, x='price')
st.plotly_chart(fig)