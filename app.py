import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px


st.set_page_config(layout='wide')
df=pd.read_csv('India.csv')
list_of_states=list(df['State'].unique())
list_of_states.insert(0,'Overall India')

st.sidebar.title('India Data Analysis')
selected_state=st.sidebar.selectbox('Select State',list_of_states)
primary=st.sidebar.selectbox('Select Primary Parameter',sorted(df.columns[5:]))
secondary=st.sidebar.selectbox('Select Secondary Parameter',sorted(df.columns[5:]))
plot=st.sidebar.button('Plot Graph')

if plot:
    st.text('Size Represent Primary Parameters')
    st.text('Color Represent Secondary Parameters')

    if selected_state=='Overall India':
        #plot the graph for india
        fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", zoom=3,size=primary,
                                color=secondary,width=1200,height=700,hover_name='District',
                                mapbox_style="carto-positron")
        st.plotly_chart(fig,use_container_width=True)
    else:
        state_df=df[df['State']==selected_state]
        fig = px.scatter_mapbox(state_df, lat="Latitude", lon="Longitude", zoom=7, size=primary,
                                color=secondary, width=1200, height=700,hover_name='District',
                                mapbox_style="carto-positron")
        st.plotly_chart(fig,use_container_width=True)
