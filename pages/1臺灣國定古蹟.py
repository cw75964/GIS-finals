import streamlit as st
import leafmap.foliumap as leafmap
import numpy as np
import pandas as pd

st.set_page_config(layout="wide")

st.title("古蹟級別選單")

old_na=pd.read_csv('https://github.com/cw75964/GIS-finals/raw/refs/heads/master/%E5%8F%A4%E8%B9%9F%E7%94%A8%E9%80%94%E3%80%81%E7%B8%A3%E5%B8%82%E3%80%81%E5%9C%B0%E5%9D%80.csv')
build_na=pd.read_csv('https://github.com/cw75964/GIS-finals/raw/refs/heads/master/%E6%AD%B7%E5%8F%B2%E5%BB%BA%E7%AF%89%E7%94%A8%E9%80%94%E3%80%81%E7%B8%A3%E5%B8%82%E3%80%81%E5%9C%B0%E5%9D%80.csv')
old_na=old_na.drop(['addresses','num'],axis=1)
build_na=build_na.drop(['addresses','num'],axis=1)

lv_option_list = old_na["assetsClassifyName"].unique().tolist()
lv_option = st.multiselect("選擇級別", lv_option_list)

if lv_option:
            old_lv_filtered = old_na[old_na["assetsClassifyName"].isin(lv_option)]
else:
            old_lv_filtered = old_na
st.subheader("臺灣古蹟 Marker Cluster")
m1 = leafmap.Map(center=[23.7652,120.4980],zoom=8,
            locate_control=True, latlon_control=True, draw_export=True, minimap_control=True)
m1.add_basemap("OpenTopoMap")
m1.add_points_from_xy(old_lv_filtered,x='longitude',y='latitude',spin=True,add_legend=True,layer_name='臺灣古蹟')
m1.to_streamlit(height=700)
st.subheader("資料表")
st.dataframe(old_lv_filtered)
st.subheader("以過去用途統計之長條圖")
old_lv_use=old_lv_filtered['name'].value_counts()
st.bar_chart(old_lv_filtered)
st.subheader("臺灣古蹟分布 Heatmap")
old_lv_filtered['num']=10
m2 = leafmap.Map(center=[23.7652,120.4980],zoom=8,locate_control=True, latlon_control=True, draw_export=True, minimap_control=True)
m2.add_heatmap(old_lv_filtered,latitude="latitude",longitude="longitude",value="num",name="古蹟分布Heat map",radius=15,)
m2.to_streamlit(height=700)

