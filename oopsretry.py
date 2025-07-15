import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# 데이터 로드
try:
    data = pd.read_csv("combined_deforestation_species.csv")
    st.success("✅ 데이터 로드 성공")
except FileNotFoundError:
    st.error("❌ 데이터 파일을 찾을 수 없습니다. CSV 파일이 같은 폴더에 있는지 확인하세요.")
    st.stop()

# Streamlit 제목
st.title("🌳 Deforestation & Threatened Species Trends")
st.write("연도별 산림 파괴율(%)과 멸종위기종 개체 수를 시각화합니다.")

# 연도 슬라이더
years = data['Year']
start_year, end_year = st.slider(
    "연도 범위 선택",
    min_value=int(years.min()),
    max_value=int(years.max()),
    value=(int(years.min()), int(years.max()))
)

# 선택한 범위 데이터 필터링
filtered = data[(data['Year'] >= start_year) & (data['Year'] <= end_year)]

# 필터 결과 확인
if filtered.empty:
    st.warning("⚠️ 선택한 연도 범위에 데이터가 없습니다. 범위를 다시 지정해 주세요.")
else:
    # 그래프 그리기
    fig = go.Figure()

    # ✅ Forest Loss (%) - 꺾은선
    fig.add_trace(go.Scatter(
        x=filtered['Year'],
        y=filtered['Forest Loss (%)'],
        name='Forest Loss Rate (%)',
        mode='lines+markers',
        line=dict(color='green', width=3)
    ))

    # ✅ Threatened Species - 막대그래프
    fig.add_trace(go.Bar(
        x=filtered['Year'],
        y=filtered['Threatened Species'],
        name='Threatened Species Count',
        marker=dict(color='rgba(255, 0, 0, 0.6)'),
        yaxis='y2'
    ))

    # 레이아웃
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

    st.plotly_chart(fig, use_container_width=True)
