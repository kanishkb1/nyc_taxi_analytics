import streamlit as st
import pandas as pd


def run(df):
    st.title("Single-column Selection")
    col = st.selectbox("Select one column:",df.columns)
    st.write('You selected:', col)
    st.write(df[col].unique())

    st.title("Multi-column Selection")

    cols = st.multiselect('Select column(s): ', df.columns,default=[])
    st.write('You Selected:', cols)

    st.write(df[cols])

