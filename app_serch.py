from operator import contains
import streamlit as st
import pandas as pd
from PIL import Image


def run_serch() :

    img2 = Image.open('data/img2.jpg')
    st.sidebar.image(img2, width=297)

    st.title('차량 검색')

    img = Image.open('data/img5.jpg')
    st.image(img, width=1420)

    df = pd.read_csv('data/car_price_sales.csv', index_col=0)


    df1 = sorted(list(df['제조사명'].unique()))
    choice = st.sidebar.selectbox('브랜드 선택', df1)
    df2 = df.groupby('제조사명').get_group(choice)
    df2_list = sorted(df2['모델'].unique())
    choice2 = st.sidebar.selectbox('모델 선택', df2_list)
    st.dataframe( df2.loc[ df2['모델'] == choice2 ].sort_values( '가격(\)', ascending=False ) )
    

    
       
    
