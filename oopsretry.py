import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 데이터 불러오기
data = pd.read_csv("combined_deforestation_species.csv")

# 제목
st.title("🌱 Global Deforestation & Threatened Species Trends")
st.write("연도별 산림 파괴율과 멸종위기종 증가율 비교")

# 연도 슬라이더
years = data['Year']
start_year, end_year = st.slider(
    "연도 범위 선택",
    min_value=int(years.min()),
    max_value=int(years.max()),
    value=(int(years.min()), int(years.max()))
)

# 선택한 범위로 데이터 필터링
filtered = data[(data['Year'] >= start_year) & (data['Year'] <= end_year)]

# 그래프 그리기
fig, ax1 = plt.subplots(figsize=(10, 6))

# 산림 파괴율 (좌측 Y축)
ax1.plot(filtered['Year'], filtered['Forest Loss (%)'], color='green', label='Forest Loss Rate (%)')
ax1.set_xlabel('Year')
ax1.set_ylabel('Forest Loss Rate (%)', color='green')
ax1.tick_params(axis='y', labelcolor='green')

# 멸종위기종 증가율 (우측 Y축)
ax2 = ax1.twinx()
ax2.plot(filtered['Year'], filtered['Threatened Growth (%)'], color='red', label='Threatened Species Growth Rate (%)')
ax2.set_ylabel('Threatened Species Growth Rate (%)', color='red')
ax2.tick_params(axis='y', labelcolor='red')

fig.suptitle('Deforestation vs Threatened Species Growth', fontsize=16)
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

st.pyplot(fig)

