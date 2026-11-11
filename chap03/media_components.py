
import streamlit as st

# 인터넷 이미지 표시
st.image('https://dimg.donga.com/wps/NEWS/IMAGE/2022/01/28/111500268.2.jpg', caption='예시 이미지')
# st.image('abc.jpg', caption='예시 이미지')

# 로컬 이미지 파일 표시 (파일이 있는 경우)
st.image('C:/Users/user/Pictures/Screenshots/my_image.jpg', caption='내 이미지')

# 오디오 파일 재생
st.audio('C:/Users/user/Music/my_audio.mp3')
# 비디오 파일 재생  
st.video('C:/Users/user/Videos/my_video.mp4')

# 유튜브 비디오 표시
st.video('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
