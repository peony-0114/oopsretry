import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# 데이터 불러오기
data = pd.read_csv("combined_deforestation_species.csv")

st.title("🌱 Deforestation & Threatened Species Trends")
st.write("연도별 산림 파괴율(%)과 멸종위기종 개체 수를 함께 시각화합니다.")

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

# 그래프 (Plotly)
fig = go.Figure()

# ✅ Forest Loss (%) - 꺾은선그래프 (좌측 Y축)
fig.add_trace(go.Scatter(
    x=filtered['Year'],
    y=filtered['Forest Loss (%)'],
    name='Forest Loss Rate (%)',
    yaxis='y1',
    mode='lines+markers',
    line=dict(color='green', width=3)
))

# ✅ Threatened Species - 막대그래프 (우측 Y축)
fig.add_trace(go.Bar(
    x=filtered['Year'],
    y=filtered['Threatened Species'],
    name='Threatened Species Count',
    yaxis='y2',
    marker=dict(color='rgba(255, 0, 0, 0.5)')
))

# 레이아웃 설정
fig.update_layout(
    title="Deforestation (Line) vs Threatened Species (Bar)",
    xaxis=dict(title='Year'),
    yaxis=dict(
        title='Forest Loss Rate (%)',
        titlefont=dict(color='green'),
        tickfont=dict(color='green')
    ),
    yaxis2=dict(
        title='Threatened Species Count',
        titlefont=dict(color='red'),
        tickfont=dict(color='red'),
        overlaying='y',
        side='right'
    ),
    legend=dict(x=0.01, y=0.99),
    bargap=0.3,
    template="plotly_white"
)

# Streamlit에 그래프 표시
st.plotly_chart(fig)
