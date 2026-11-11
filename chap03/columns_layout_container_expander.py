
import streamlit as st

with st.container():
    st.subheader('이번 달 도서관 현황')
    st.write('이 영역에는 도서관의 주요 통계가 표시됩니다')
    st.metric("대출 도서 수", "1,245권")
    st.metric("신규 회원", "+23명")

with st.expander("상세 통계 정보"):
    st.write("여기에는 자세한 분석 결과가 들어갑니다")
    st.write("평소에는 숨겨져 있다가 필요할 때만 펼쳐볼 수 있습니다")
