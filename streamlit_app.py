import plotly
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import pydeck as pdk

from mystlib import viewOnMap

from mystlib import plot2D
pd.options.mode.chained_assignment = None  # default='warn'

df = pd.read_csv('dataset.csv')

st.set_page_config(layout="wide", page_title="Streamlit Data-centric App", page_icon=":taxi:")



message=""" __Select a functionality from the list below__"""
with st.sidebar:
    st.markdown(message)
    page = st.selectbox('Select:',
            ['View Data Using Dropdowns',
        'Visualize Data on a Map',
        '2D Charts and Histograms', 
        '3D Charts and Histograms'])

import preprocess

#Preprocess the dataset
preprocess.run(df)

#Do some more processing.
df = preprocess.lat_lon_conversion("mydataset.csv")

#Display interactive dataframe
st.dataframe(df)

from mystlib import explore
from mystlib import plot3D

if page == 'View Data Using Dropdowns':
    explore.run(df)
elif page == 'Visualize Data on a Map':
    viewOnMap.run(df)
elif page == '2D Charts and Histograms':
    plot2D.run(df)
elif page == '3D Charts and Histograms':
    plot3D.run(df)


