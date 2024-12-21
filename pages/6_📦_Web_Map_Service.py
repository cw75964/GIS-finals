import ast
import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

st.title('台灣文化資產失火、破壞列表(from全能古蹟燒毀王)')
st.write('這個Google my map 來源於:')
st.markdown("""<iframe src="https://www.google.com/maps/d/embed?mid=11yl4gOQPCqLQGVoHlwjy6zcOK70&hl=en_US&ehbc=2E312F" width="640" height="480"></iframe>"""
            , unsafe_allow_html=True)
