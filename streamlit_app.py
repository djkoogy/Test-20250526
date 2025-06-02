import pandas as pd
import folium
import streamlit as st
from streamlit_folium import st_folium
from streamlit_folium import folium_static
from folium.plugins import MarkerCluster



st.title("진주시 CCTV 현황")

df = pd.read_csv("jinju_cctv_20250513.csv", encoding='euc-kr')

st.dataframe(df, height=200)

df[["lat","lon"]] = df[["위도","경도"]]

m = folium.Map(location=[35.1799817, 128.1076213], zoom_start=13)

marker_cluster = MarkerCluster().add_to(m)

for idx, row in df.iterrows():
    folium.Marker(
        location=[row["lat"], row["lon"]],
        popup=row["설치장소"],
    ).add_to(marker_cluster)

st_folium(m)
# folium_static(m)