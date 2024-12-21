import streamlit as st
import leafmap.foliumap as leafmap
import numpy as np
import pandas as pd

st.set_page_config(layout="wide")

old_na=pd.read_csv('https://github.com/cw75964/GIS-finals/raw/refs/heads/master/%E5%8F%A4%E8%B9%9F%E7%94%A8%E9%80%94%E3%80%81%E7%B8%A3%E5%B8%82%E3%80%81%E5%9C%B0%E5%9D%80.csv')
build_na=pd.read_csv('https://github.com/cw75964/GIS-finals/raw/refs/heads/master/%E6%AD%B7%E5%8F%B2%E5%BB%BA%E7%AF%89%E7%94%A8%E9%80%94%E3%80%81%E7%B8%A3%E5%B8%82%E3%80%81%E5%9C%B0%E5%9D%80.csv')
old_na=old_na.drop(['addresses','num'],axis=1)
build_na=build_na.drop(['addresses','num'],axis=1)

st.title('整合之選單')
st.header('古蹟整合選單)
ocol1,ocol2,ocol3=st.columns([1, 1, 1])
with ocol1:
            city_option_list = old_na["city"].unique().tolist()
            city_option = st.multiselect("選擇縣市", city_option_list,default=city_option_list)
with ocol2:
            name_option_list = old_na["name"].unique().tolist()
            name_option = st.multiselect("選擇過去用途", name_option_list,default=name_option_list)
with ocol3:
            lv_option_list = old_na["assetsClassifyName"].unique().tolist()
            lv_option = st.multiselect("選擇級別", lv_option_list,default=lv_option_list)

filtered_old=old_na[old_na[old_na['city'].isin(city_option) & old_na['name'].isin(name_option) & old_na['assetsClassifyName'].isin(lv_option)]]
filtered_name_option_list=filtered_old['name'].unique().tolist()
name_option=st.multiselect("選擇過去用途", filtered_name_option_list, default=filtered_name_option_list)
filtered_level_option_list = filtered_old[filtered_old['name'].isin(name_option)]['assetsClassifyName'].unique().tolist()
lv_option = st.multiselect("選擇級別", filtered_level_option_list, default=filtered_level_option_list)
filtered_city_option_list=filtered_old[filtered_old['assetsClassifyName'].isin(lv_option)]['city'].unique().tolist()
city_option=st.multiselect("選擇縣市", filtered_city_option_list,default=filtered_city_option_list)

st.subheader("臺灣古蹟 Marker Cluster")
m1 = leafmap.Map(center=[23.7652,120.4980],zoom=8,
            locate_control=True, latlon_control=True, draw_export=True, minimap_control=True)
m1.add_basemap("OpenTopoMap")
m1.add_points_from_xy(filtered_old,x='longitude',y='latitude',spin=True,add_legend=True,layer_name='臺灣古蹟')
m1.to_streamlit(height=700)
st.subheader("資料表")
st.dataframe(filtered_old)
