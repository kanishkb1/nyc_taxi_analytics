import streamlit as st
import plotly.express as px

def run(df):
    st.subheader("Plot # 01:")
    fig1 = px.bar(df.groupby('passenger_count').agg('mean'),
                y = 'duration',
                title = "Mean Travel Time for No. of Passanger")

    st.plotly_chart(fig1,use_container_width=True)

    #Fig 2

    st.subheader("Plot # 02:")
    fig2 = px.scatter(
            df, x= 'duration', y = 'distance',
            color = 'passenger_count',
            title="Distance to duration relationship"
    )

    st.plotly_chart(fig2, use_container_width=True)