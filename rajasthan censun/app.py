import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

df = pd.read_csv('raj.csv')
list_of_city = list(df['District'])
list_of_city.insert(0,'over all rajasthan')

st.set_page_config(layout='wide')

st.sidebar.title('rajasthan censun data visulation ')
selected_city = st.sidebar.selectbox('select a city',list_of_city)
primary = st.sidebar.selectbox('select primary parameter',sorted(df.columns[5:]))
secondary = st.sidebar.selectbox('select secondary parameter',sorted(df.columns[5:]))
plot = st.sidebar.button('plot graph')

if plot:
    st.text('size reprsetns primary parameter')
    st.text('color reprsetns secondary parameter')
    if selected_city == 'over all rajasthan':
        fig = px.scatter_mapbox(df,lat='Latitude',lon='Longitude',size=primary,color=secondary,zoom=5,
                                size_max=25,mapbox_style='carto-positron',width=1200,height=700,hover_name='District')
        st.plotly_chart(fig,use_container_width=True)
    else:
        city_df = df[df['District'] == selected_city]
        fig = px.scatter_mapbox(city_df,lat='Latitude',lon='Longitude',size=primary,color=secondary,zoom=7,
                                size_max=25,mapbox_style='carto-positron',width=1200,height=700,hover_name='District')
        st.plotly_chart(fig,use_container_width=True)

