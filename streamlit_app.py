#libraries imported
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px
import pydeck as pdk
import preprocess

#load dataset
dataframe = pd.read_csv('dataset.csv')
#print(dataframe.head())



st.set_page_config(page_title = "New York City Taxi Traffic Analysis ",  layout = "wide",page_icon = ":taxi:")

message = """
        __Select a functionality from the list below__
        """

with st.sidebar:
    st.markdown(message)
    page = st.selectbox('Select:',['View Data Using Dropdowns','Visualize Data on a Map','2D Charts and Histograms', '3D Charts and Histograms'])

#data pre-processing (preprocess.py)
preprocess.run(dataframe)

#To store polyline latitudes and longitudes in separate lists, we are calling the lat_lon_conversion function
df = preprocess.lat_lon_conversion("mydataset.csv")


#Display interactive dataframe
st.dataframe(df)

