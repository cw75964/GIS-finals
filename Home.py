import streamlit as st
import leafmap.foliumap as leafmap
import numpy as np
import pandas as pd


st.set_page_config(layout="wide")



st.title('古蹟、歷史建築之定義')
st.write('古蹟：指人類為生活需要所營建之具有歷史、文化、藝術價值之建造物及附屬設施。')
st.write('歷史建築：指歷史事件所定著或具有歷史性、地方性、特殊性之文化、藝術價值，應予保存之建造物及附屬設施。')

st.title("臺灣古蹟、歷史建築之分布")


old_na=pd.read_csv('https://github.com/cw75964/GIS-finals/raw/refs/heads/master/%E5%8F%A4%E8%B9%9F%E7%94%A8%E9%80%94%E3%80%81%E7%B8%A3%E5%B8%82%E3%80%81%E5%9C%B0%E5%9D%80.csv')
build_na=pd.read_csv('https://github.com/cw75964/GIS-finals/raw/refs/heads/master/%E6%AD%B7%E5%8F%B2%E5%BB%BA%E7%AF%89%E7%94%A8%E9%80%94%E3%80%81%E7%B8%A3%E5%B8%82%E3%80%81%E5%9C%B0%E5%9D%80.csv')
old_na=old_na.drop(['addresses','num'],axis=1)
build_na=build_na.drop(['addresses','num'],axis=1)


old_name=old_na['name'].value_counts()
old_city=old_na['city'].value_counts()
build_name=build_na['name'].value_counts()
build_city=build_na['city'].value_counts()

st.subheader("散佈圖")
mcol1,mcol2=st.columns([1,1])
with mcol1:
            st.subheader('古蹟')
            st.map(old_na, size=20, color="#D94600")
with mcol2:
            st.subheader('歷史建築')
            st.map(build_na, size=20, color="#2828FF")
st.subheader("Marker Cluster")
m1 = leafmap.Map(center=[23.7652,120.4980],zoom=8,
            locate_control=True, latlon_control=True, draw_export=True, minimap_control=True)
m1.add_points_from_xy(old_na,x='longitude',y='latitude',spin=True,add_legend=True,layer_name='臺灣古蹟')
m1.add_points_from_xy(build_na,x='longitude',y='latitude',spin=True,add_legend=True,layer_name='臺灣歷史建築')
m1.to_streamlit(height=700)
st.subheader("資料表")
col1,col2=st.columns([1,1])
with col1:
            st.subheader('古蹟')
            st.dataframe(old_na)
with col2:
            st.subheader('歷史建築')
            st.dataframe(build_na)
st.subheader("以過去用途統計之長條圖")
ncol1,ncol2=st.columns([1,1])
with ncol1:
            st.subheader('古蹟')
            st.bar_chart(old_name)
with ncol2:
            st.subheader('歷史建築')
            st.bar_chart(build_name)
st.subheader("Heatmap")
old_na['num']=10
build_na['num']=10
m2 = leafmap.Map(center=[23.7652,120.4980],zoom=8,locate_control=True, latlon_control=True, draw_export=True, minimap_control=True)
m2.add_heatmap(old_na,latitude="latitude",longitude="longitude",value="num",name="古蹟分布Heat map",radius=15,)
m2.add_heatmap(build_na,latitude="latitude",longitude="longitude",value="num",name="歷史建築分布Heat map",radius=15,)
m2.to_streamlit(height=700)
st.subheader('以縣市統計之長條圖')
ccol1,ccol2=st.columns([1,1])
with ccol1:
            st.subheader('古蹟')
            st.bar_chart(old_city)
with ccol2:
            st.subheader('歷史建築')
            st.bar_chart(build_city)
