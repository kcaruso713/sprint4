import streamlit as st # type: ignore
import pandas as pd # type: ignore
import plotly.express as px # type: ignore

# Ensure the dataset path is relative to the root directory.
df = pd.read_csv('vehicles_us_2.csv')



df.drop_duplicates # Check for duplicates

df.duplicates().sum() # Check for duplicates



#Handle missing values for 'model_year' using median
df['model_year'] = df['model_year'].fillna(df['model_year'].median())

# Fill 'cylinders' with the median within each 'model'
df['cylinders'] = df.groupby('model')['cylinders'].transform(lambda x: x.fillna(x.median()))

# Fill 'odometer' with the median within each 'model'
df['odometer'] = df.groupby('model')['odometer'].transform(lambda x: x.fillna(x.median()))

# Fill 'paint_color' with 'Unknown'
df['paint_color'] = df['paint_color'].fillna('Unknown')
print(df.dtypes)



 # Convert 'price' column to numeric
df['price'] = pd.to_numeric(df['price'], errors='coerce')
df = df.dropna(subset=['price'])

   # Now plot the histogram
st.header("My Data Dashboard")
fig = px.histogram(df, x='price', nbins=50)
st.plotly_chart(fig)

# Scatter plot
st.header("Scatter Plot")
fig_2 = px.scatter(df, x='odometer', y='price', title='Price vs Odometer')
st.plotly_chart(fig_2)

show_histogram = st.checkbox('Show Histogram')

if show_histogram:
    st.plotly_chart(fig)