import streamlit as st
import leafmap.foliumap as leafmap
import numpy as np
import pandas as pd

st.set_page_config(layout="wide")

old_na=pd.read_csv('https://github.com/cw75964/GIS-finals/raw/refs/heads/master/%E5%8F%A4%E8%B9%9F%E7%94%A8%E9%80%94%E3%80%81%E7%B8%A3%E5%B8%82%E3%80%81%E5%9C%B0%E5%9D%80.csv')
build_na=pd.read_csv('https://github.com/cw75964/GIS-finals/raw/refs/heads/master/%E6%AD%B7%E5%8F%B2%E5%BB%BA%E7%AF%89%E7%94%A8%E9%80%94%E3%80%81%E7%B8%A3%E5%B8%82%E3%80%81%E5%9C%B0%E5%9D%80.csv')
old_na=old_na.drop(['num'],axis=1)
build_na=build_na.drop(['num'],axis=1)

st.title('整合之選單')
ocol1,ocol2,ocol3=st.columns([1, 1, 1])
with ocol1:
            city_option_list = ['臺北市','新北市','基隆市','桃園市','新竹市','新竹縣','苗栗縣','臺中市','彰化縣','南投縣','雲林縣','嘉義市','嘉義縣','臺南市','高雄市','屏東縣','宜蘭縣','花蓮縣','臺東縣','澎湖縣','金門縣','連江縣']
            city_option = st.multiselect("選擇縣市", city_option_list,default=[])
with ocol2:
            name_option_list = ['宅第', '其他設施', '寺廟', '墓葬', '衙署', '碑碣', '產業', '祠堂', '橋樑', '關塞', '牌坊','學校', '城郭', '車站', '書院', '教堂', '燈塔', '商店', '醫院', '辦公廳舍', '機關', '堤閘','官邸', '銀行', '集會堂', '戲劇院', '博物館', '市場']
            name_option = st.multiselect("選擇過去用途", name_option_list,default=[])
with ocol3:
            lv_option_list = old_na["assetsClassifyName"].unique().tolist()
            lv_option = st.multiselect("選擇級別", lv_option_list,default=[])
filtered_old = old_na
filtered_build=build_na

if len(city_option) > 0:
            filtered_old = filtered_old[filtered_old["city"].isin(city_option)]
            filtered_build = filtered_build[filtered_build["city"].isin(city_option)]

if len(name_option) > 0:
            filtered_old = filtered_old[filtered_old["name"].isin(name_option)]
            filtered_build = filtered_build[filtered_build["name"].isin(name_option)]

if len(lv_option) > 0:
            filtered_old = filtered_old[filtered_old["assetsClassifyName"].isin(lv_option)]
district_option_list=filtered_old['district'].unique().tolist()+filtered_build['district'].unique().tolist()
district_option=st.multiselect("選擇過去用途", district_option_list,default=[])
if district_option:
            filtered_old= filtered_old[filtered_old["district"].isin(district_option)]
            filtered_build = filtered_build[filtered_build["district"].isin(district_option)]
else:
            filtered_old = filtered_old
            filtered_build = filtered_build
col1, col2 = st.columns([1, 1])
with col1:
            st.subheader("臺灣古蹟 Marker Cluster")
            m1 = leafmap.Map(center=[23.7652,120.4980],zoom=8,
                        locate_control=True, latlon_control=True, draw_export=True, minimap_control=True)
            m1.add_basemap("OpenTopoMap")
            m1.add_points_from_xy(filtered_old,x='longitude',y='latitude',spin=True,add_legend=True,layer_name='臺灣古蹟')
            m1.to_streamlit(height=700)
            st.subheader("資料表")
            st.dataframe(filtered_old)
            st.subheader("臺灣古蹟散佈圖")
            st.map(filtered_old, size=20, color="#D94600")
            st.subheader("臺灣古蹟分布 Heatmap")
            filtered_old['num']=10
            m2 = leafmap.Map(center=[23.7652,120.4980],zoom=8,locate_control=True, latlon_control=True, draw_export=True, minimap_control=True)
            m2.add_heatmap(filtered_old,latitude="latitude",longitude="longitude",value="num",name="古蹟分布Heat map",radius=15,)
            m2.to_streamlit(height=700)
with col2:
            st.subheader("臺灣歷史建築 Marker Cluster")
            m3 = leafmap.Map(center=[23.7652,120.4980],zoom=8,
                        locate_control=True, latlon_control=True, draw_export=True, minimap_control=True)
            m3.add_basemap("OpenTopoMap")
            m3.add_points_from_xy(filtered_build,x='longitude',y='latitude',spin=True,add_legend=True,layer_name='臺灣歷史建築')
            m3.to_streamlit(height=700)
            st.subheader("資料表")
            st.dataframe(filtered_build)
            st.subheader("臺灣歷史建築散佈圖")
            st.map(filtered_build, size=20, color="#2828FF")
            st.subheader("臺灣歷史建築分布 Heatmap")
            filtered_build['num']=10
            m4 = leafmap.Map(center=[23.7652,120.4980],zoom=8,locate_control=True, latlon_control=True, draw_export=True, minimap_control=True)
            m4.add_heatmap(filtered_build,latitude="latitude",longitude="longitude",value="num",name="歷史建築分布Heat map",radius=15,)
            m4.to_streamlit(height=700)
            


