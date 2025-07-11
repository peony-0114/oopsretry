import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# 데이터 불러오기
data = pd.read_csv("combined_deforestation_species.csv")

st.title("🌳 Deforestation & Threatened Species Trends")
st.write("연도별 산림 파괴율(%)과 멸종위기종 개체 수를 함께 시각화합니다.")

# 연도 슬라이더
years = data['Year']
start_year, end_year = st.slider(
    "연도 범위 선택",
    min_value=int(years.min()),
    max_value=int(years.max()),
    value=(int(years.min()), int(years.max()))
)

# 선택한 범위로 데이터 필
