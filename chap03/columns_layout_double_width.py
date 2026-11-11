
import streamlit as st

# 첫 번째 열을 다른 열보다 2배 크게 만들기
col1, col2, col3 = st.columns([2, 1, 1])

with col1:
    st.write('메인 콘텐츠 영역 - 이 열이 가장 넓습니다')

with col2:
    st.write('통계 정보')

with col3:
    st.write('빠른 메뉴')
