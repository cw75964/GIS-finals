import streamlit as st
import leafmap.foliumap as leafmap
import numpy as np
import pandas as pd

st.set_page_config(layout="wide")


st.title("臺灣古蹟、歷史建築過去用途之選單")


old_na=pd.read_csv('https://github.com/cw75964/GIS-finals/raw/refs/heads/master/%E5%8F%A4%E8%B9%9F%E7%94%A8%E9%80%94%E3%80%81%E7%B8%A3%E5%B8%82%E3%80%81%E5%9C%B0%E5%9D%80.csv')
build_na=pd.read_csv('https://github.com/cw75964/GIS-finals/raw/refs/heads/master/%E6%AD%B7%E5%8F%B2%E5%BB%BA%E7%AF%89%E7%94%A8%E9%80%94%E3%80%81%E7%B8%A3%E5%B8%82%E3%80%81%E5%9C%B0%E5%9D%80.csv')
old_na=old_na.drop(['num'],axis=1)
build_na=build_na.drop(['num'],axis=1)

name_option_list = ['宅第', '其他設施', '寺廟', '墓葬', '衙署', '碑碣', '產業', '祠堂', '橋樑', '關塞', '牌坊','學校', '城郭', '車站', '書院', '教堂', '燈塔', '商店', '醫院', '辦公廳舍', '機關', '堤閘','官邸', '銀行', '集會堂', '戲劇院', '博物館', '市場']
name_option = st.multiselect("選擇過去用途", name_option_list)

if name_option:
            old_name_filtered = old_na[old_na["name"].isin(name_option)]
            build_name_filtered=build_na[build_na["name"].isin(name_option)]            
else:
            old_name_filtered = old_na
            build_name_filtered=build_na

col1, col2 = st.columns([1, 1])
with col1:
            st.subheader("臺灣古蹟 Marker Cluster")
            m1 = leafmap.Map(center=[23.7652,120.4980],zoom=8,
                        locate_control=True, latlon_control=True, draw_export=True, minimap_control=True)
            m1.add_basemap("OpenTopoMap")
            m1.add_points_from_xy(old_name_filtered,x='longitude',y='latitude',spin=True,add_legend=True,layer_name='臺灣古蹟')
            m1.to_streamlit(height=700)
            st.subheader("資料表")
            st.dataframe(old_name_filtered)
            st.subheader("臺灣古蹟散佈圖")
            st.map(old_name_filtered, size=20, color="#D94600")
            st.subheader("臺灣古蹟分布 Heatmap")
            old_name_filtered['num']=10
            m2 = leafmap.Map(center=[23.7652,120.4980],zoom=8,locate_control=True, latlon_control=True, draw_export=True, minimap_control=True)
            m2.add_heatmap(old_name_filtered,latitude="latitude",longitude="longitude",value="num",name="古蹟分布Heat map",radius=15,)
            m2.to_streamlit(height=700)
            st.subheader('以縣市統計之長條圖')
            old_city=old_name_filtered['city'].value_counts()
            st.bar_chart(old_city)
            st.subheader("以古蹟級別統計之長條圖")
            level=old_name_filtered['assetsClassifyName'].value_counts().reset_index()
            level.columns=['name','count']
            fig3= px.pie(level, names='name', values='count')
            st.plotly_chart(fig3)


with col2:
            st.subheader("臺灣歷史建築 Marker Cluster")
            m3 = leafmap.Map(center=[23.7652,120.4980],zoom=8,
                        locate_control=True, latlon_control=True, draw_export=True, minimap_control=True)
            m3.add_basemap("OpenTopoMap")
            m3.add_points_from_xy(build_name_filtered,x='longitude',y='latitude',spin=True,add_legend=True,layer_name='臺灣歷史建築')
            m3.to_streamlit(height=700)
            st.subheader("資料表")
            st.dataframe(build_name_filtered)
            st.subheader("臺灣歷史建築散佈圖")
            st.map(build_name_filtered, size=20, color="#2828FF")
            st.subheader("臺灣歷史建築分布 Heatmap")
            build_name_filtered['num']=10
            m4 = leafmap.Map(center=[23.7652,120.4980],zoom=8,locate_control=True, latlon_control=True, draw_export=True, minimap_control=True)
            m4.add_heatmap(build_name_filtered,latitude="latitude",longitude="longitude",value="num",name="歷史建築分布Heat map",radius=15,)
            m4.to_streamlit(height=700)
            city=st.subheader('以縣市統計之長條圖')
            build_city=build_name_filtered['city'].value_counts()
            st.bar_chart(build_city)
