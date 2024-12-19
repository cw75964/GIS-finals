import streamlit as st
import leafmap.foliumap as leafmap
import numpy as np
import pandas as pd

st.set_page_config(layout="wide")

markdown = """
Web App URL: <https://geotemplate.streamlit.app>
GitHub Repository: <https://github.com/giswqs/streamlit-multipage-template>
"""

old_na=pd.read_csv('https://github.com/cw75964/GIS-finals/raw/refs/heads/master/%E5%8F%A4%E8%B9%9F%E7%94%A8%E9%80%94%E3%80%81%E7%B8%A3%E5%B8%82.csv')
build_na=pd.read_csv('https://github.com/cw75964/GIS-finals/raw/refs/heads/master/%E6%AD%B7%E5%8F%B2%E5%BB%BA%E7%AF%89%E7%94%A8%E9%80%94%E3%80%81%E7%B8%A3%E5%B8%82.csv')
dwell_old=old_na[old_na['name')=='宅第']
dwell_build=build_na[build_na['name']=='宅第']
old_maker=dwell_old.drop(['name','city'],axis=1)
build_maker=dwell_build.drop(['name','city'],axis=1)
dw_old_city=dwell_old['city'].value_counts()
dw_build_city=dwell_build['city'].value_counts()
st.title("臺灣宅第")

st.header("宅第(古蹟)Marker Cluster")

m1 = leafmap.Map(center=[23.7652,120.4980],zoom=8,
            locate_control=True, latlon_control=True, draw_export=True, minimap_control=True)
m1.add_basemap("OpenTopoMap")
m1.add_points_from_xy(old_maker,x='longitude',y='latitude',spin=True,add_legend=True,layer_name='宅第(古蹟)')
m1.to_streamlit(height=700)
st.dataframe(old_maker)
st.header("宅第(古蹟)Heatmap")
dwell_old['num']=10
m2 = leafmap.Map(center=[23.7652,120.4980],zoom=8,
            locate_control=True, latlon_control=True, draw_export=True, minimap_control=True
            )
m2.add_heatmap(dwell_old,
              latitude="latitude",longitude="longitude",value="num",name="Heat map",radius=20,)
m2.to_streamlit(height=700)
st.bar_chart(dw_old_city)

st.header("宅第(歷史建築)Marker Cluster")

m3 = leafmap.Map(center=[23.7652,120.4980],zoom=8,
            locate_control=True, latlon_control=True, draw_export=True, minimap_control=True)
m3.add_basemap("OpenTopoMap")
m3.add_points_from_xy(build_maker,x='longitude',y='latitude',spin=True,add_legend=True,layer_name='宅第(歷史建築)')
m3.to_streamlit(height=700)
st.dataframe(build_maker)
st.header("宅第(歷史建築)Heatmap")
dwell_old['num']=10
m4 = leafmap.Map(center=[23.7652,120.4980],zoom=8,
            locate_control=True, latlon_control=True, draw_export=True, minimap_control=True
            )
m4.add_heatmap(dwell_build,
              latitude="latitude",longitude="longitude",value="num",name="Heat map",radius=20,)
m4.to_streamlit(height=700)
st.bar_chart(dw_build_city)



