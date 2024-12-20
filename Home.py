import streamlit as st
import leafmap.foliumap as leafmap
import numpy as np
import pandas as pd


st.set_page_config(layout="wide")

# Customize the sidebar
markdown = """
Web App URL: <https://geotemplate.streamlit.app>
GitHub Repository: <https://github.com/giswqs/streamlit-multipage-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

# Customize page title
st.title('古蹟、歷史建築之定義')
st.write('古蹟：指人類為生活需要所營建之具有歷史、文化、藝術價值之建造物及附屬設施。')
st.write('歷史建築：指歷史事件所定著或具有歷史性、地方性、特殊性之文化、藝術價值，應予保存之建造物及附屬設施。')

st.title("臺灣古蹟、歷史建築之分布")

old=pd.read_csv('https://github.com/cw75964/GIS-finals/raw/refs/heads/master/%E5%8F%B0%E7%81%A3%E5%8F%A4%E8%B9%9F%20%E4%BF%AE%E6%AD%A3.csv')
building=pd.read_csv('https://github.com/cw75964/GIS-finals/raw/refs/heads/master/%E5%8F%B0%E7%81%A3%E6%AD%B7%E5%8F%B2%E5%BB%BA%E7%AF%89%20%E4%BF%AE%E6%AD%A3.csv')
old_na=pd.read_csv('https://github.com/cw75964/GIS-finals/raw/refs/heads/master/%E5%8F%A4%E8%B9%9F%E7%94%A8%E9%80%94%E3%80%81%E7%B8%A3%E5%B8%82.csv')
build_na=pd.read_csv('https://github.com/cw75964/GIS-finals/raw/refs/heads/master/%E6%AD%B7%E5%8F%B2%E5%BB%BA%E7%AF%89%E7%94%A8%E9%80%94%E3%80%81%E7%B8%A3%E5%B8%82.csv')

old_name=old_na['name'].value_counts()
old_city=old_na['city'].value_counts()
build_name=build_na['name'].value_counts()
build_city=build_na['city'].value_counts()

st.header("臺灣古蹟 Marker Cluster")
m1 = leafmap.Map(center=[23.7652,120.4980],zoom=8,
            locate_control=True, latlon_control=True, draw_export=True, minimap_control=True
            )
m1.add_basemap("OpenTopoMap")
m1.add_points_from_xy(old,x='longitude',y='latitude',spin=True,add_legend=True,layer_name='臺灣古蹟')
m1.to_streamlit(height=700)
st.write(old)
st.bar_chart(old_name)

st.header("臺灣古蹟分布 Heatmap")
with st.expander("See source code"):
    with st.echo():
        old['num']=10
        m2 = leafmap.Map(center=[23.7652,120.4980],zoom=8,locate_control=True, latlon_control=True, draw_export=True, minimap_control=True)
        m2.add_basemap("OpenTopoMap")
        m2.add_heatmap(old,latitude="latitude",longitude="longitude",value="num",name="古蹟分布Heat map",radius=15,)
m2.to_streamlit(height=700)
st.bar_chart(old_city)

st.header("臺灣歷史建築 Marker Cluster")
m3 = leafmap.Map(center=[23.7652,120.4980],zoom=8,
            locate_control=True, latlon_control=True, draw_export=True, minimap_control=True
            )
m3.add_basemap("OpenTopoMap")
m3.add_points_from_xy(building,x='longitude',y='latitude',spin=True,add_legend=True,layer_name='臺灣歷史建築')
m3.to_streamlit(height=700)
st.write(building)
st.bar_chart(build_name)
st.header("臺灣歷史建築分布 Heatmap")
with st.expander("See source code"):
    with st.echo():
        building['num']=10
        m4 = leafmap.Map(center=[23.7652,120.4980],zoom=8,locate_control=True, latlon_control=True, draw_export=True, minimap_control=True)
        m4.add_basemap("OpenTopoMap")
        m4.add_heatmap(building,latitude="latitude",longitude="longitude",value="num",name="歷史建築分布Heat map",radius=15,)
m4.to_streamlit(height=700)
st.bar_chart(build_city)
