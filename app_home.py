import streamlit as st
from PIL import Image


def run_home() :

    img = Image.open('data/img4.jpg')
    st.sidebar.image(img, width=297)

    st.title('The Purchase of a Used Car')
    st.video('https://www.youtube.com/watch?v=UZs758DjFgI')

    st.info('차량 검색기능, EDA, 고객 데이터를 기반으로 구매가능 금액 예측 및 추천, 신규 입고 차량을 추가 등록하는 기능을 구현한 앱입니다.')