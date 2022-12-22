import pandas as pd
import streamlit as st

def run(dataframe):
    st.title("Single-column Selection")
    col = st.selectbox('Please select one column.',dataframe.columns)
    st.write('You have selected',col)
    st.write(dataframe[col].unique())


    st.title("Single-column Selection")
    cols = st.multiselect('select column(s):', dataframe.columns, default = [])
    st.write('You selected:', cols)
    st.write(dataframe[cols])


