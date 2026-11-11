
import streamlit as st

st.title('학생 정보 관리 시스템')

# 4개의 열로 나누기
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("전체 학생 수", "245명")

with col2:
    st.metric("평균 점수", "82.5점")

with col3:
    st.metric("출석률", "94.2%")

with col4:
    st.metric("과제 제출률", "87.8%")
