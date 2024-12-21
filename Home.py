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
old_na=pd.read_csv('https://github.com/cw75964/GIS-finals/raw/refs/heads/master/%E5%8F%A4%E8%B9%9F%E7%94%A8%E9%80%94%E3%80%81%E7%B8%A3%E5%B8%82%E3%80%81%E5%9C%B0%E5%9D%80.csv')
build_na=pd.read_csv('https://github.com/cw75964/GIS-finals/raw/refs/heads/master/%E6%AD%B7%E5%8F%B2%E5%BB%BA%E7%AF%89%E7%94%A8%E9%80%94%E3%80%81%E7%B8%A3%E5%B8%82%E3%80%81%E5%9C%B0%E5%9D%80.csv')
old_na.drop(columns=['addresses','num'])
build_na.drop(columns=['addresses','num'])


old_name=old_na['name'].value_counts()
old_city=old_na['city'].value_counts()
build_name=build_na['name'].value_counts()
build_city=build_na['city'].value_counts()

city_option_list = old_na["city"].unique().tolist()
city_option = st.multiselect("選擇縣市", city_option_list)

if city_option:
            old_city_filtered = old_na[old_na["city"].isin(city_option)]
            build_city_filtered=build_na[build_na["city"].isin(city_option)]            
else:
            old_city_filtered = old_na
            build_city_filtered=build_na

col1, col2 = st.columns([1, 1])
with col1:
            st.subheader("臺灣古蹟 Marker Cluster")
            m1 = leafmap.Map(center=[23.7652,120.4980],zoom=8,
                        locate_control=True, latlon_control=True, draw_export=True, minimap_control=True)
            m1.add_basemap("OpenTopoMap")
            m1.add_points_from_xy(old_city_filtered,x='longitude',y='latitude',spin=True,add_legend=True,layer_name='臺灣古蹟')
            m1.to_streamlit(height=700)
            st.dataframe(old_city_filtered)
            old_city_name=old_city_filtered['name'].value_counts()
            st.bar_chart(old_city_name)
            st.subheader("臺灣古蹟分布 Heatmap")
            old_city_filtered['num']=10
            m2 = leafmap.Map(center=[23.7652,120.4980],zoom=8,locate_control=True, latlon_control=True, draw_export=True, minimap_control=True)
            m2.add_heatmap(old_city_filtered,latitude="latitude",longitude="longitude",value="num",name="古蹟分布Heat map",radius=15,)
            m2.to_streamlit(height=700)
            st.bar_chart(old_city)

with col2:
            st.subheader("臺灣歷史建築 Marker Cluster")
            m3 = leafmap.Map(center=[23.7652,120.4980],zoom=8,
                        locate_control=True, latlon_control=True, draw_export=True, minimap_control=True)
            m3.add_basemap("OpenTopoMap")
            m3.add_points_from_xy(build_city_filtered,x='longitude',y='latitude',spin=True,add_legend=True,layer_name='臺灣歷史建築')
            m3.to_streamlit(height=700)
            st.dataframe(build_city_filtered)
            build_city_name=build_city_filtered['name'].value_counts()
            st.bar_chart(build_city_name)
            st.header("臺灣歷史建築分布 Heatmap")
            build_city_filtered['num']=10
            m4 = leafmap.Map(center=[23.7652,120.4980],zoom=8,locate_control=True, latlon_control=True, draw_export=True, minimap_control=True)
            m4.add_heatmap(build_city_filtered,latitude="latitude",longitude="longitude",value="num",name="歷史建築分布Heat map",radius=15,)
            m4.to_streamlit(height=700)
            st.bar_chart(build_city)
