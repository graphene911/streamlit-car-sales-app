import streamlit as st
from PIL import Image


def run_home() :

    img = Image.open('data\img4.jpg')
    st.sidebar.image(img, width=297)

    st.title('The Purchase of a Used Car')
    st.video('https://www.youtube.com/watch?v=UZs758DjFgI')