import streamlit as st
import leafmap.foliumap as leafmap
import numpy as np
import pandas as pd
markdown = """
Web App URL: <https://geotemplate.streamlit.app>
GitHub Repository: <https://github.com/giswqs/streamlit-multipage-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)


st.title("臺灣國定古蹟")

st.header("Marker Cluster")
old=pd.read_csv('https://github.com/cw75964/GIS-finals/raw/refs/heads/master/%E5%8F%B0%E7%81%A3%E5%8F%A4%E8%B9%9F%20%E4%BF%AE%E6%AD%A3.csv')
nation_old=old[old[assetsClassifyName]=="國定古蹟"]
m1 = leafmap.Map(center=[23.7652,120.4980],zoom=8,
            locate_control=True, latlon_control=True, draw_export=True, minimap_control=True)
m1.add_basemap("OpenTopoMap")
m1.add_points_from_xy(nation_old,x='longitude',y='latitude',spin=True,add_legend=True,layer_name='國定古蹟')
m1.to_streamlit(height=700)
st.write(national_old)
st.header("Heatmap")
nation_old['num']=10
m2 = leafmap.Map(center=[23.7652,120.4980],zoom=8,
            locate_control=True, latlon_control=True, draw_export=True, minimap_control=True
            )
m2.add_basemap("OpenTopoMap")
m2.add_heatmap(nation_old,
              latitude="latitude",longitude="longitude",value="num",name="Heat map",radius=15,)
m2.to_streamlit(height=700)
