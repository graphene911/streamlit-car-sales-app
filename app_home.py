from operator import contains
import streamlit as st
import pandas as pd
import joblib
import numpy as np
import sklearn
from sklearn.linear_model import LinearRegression

def run_home() :
    st.title('고객 정보 입력을 통한 차량 구매가능 금액 예측 및 추천 앱 입니다.')

    st.subheader('차량 검색')
    df = pd.read_csv('data/car_price_sales.csv', index_col=0)


    df1 = sorted(list(df['제조사명'].unique()))
    choice = st.sidebar.selectbox('브랜드 선택', df1)
    df2 = df.groupby('제조사명').get_group(choice)
    df2_list = sorted(df2['모델'].unique())
    choice2 = st.sidebar.selectbox('모델 선택', df2_list)
    st.dataframe( df2.loc[ df2['모델'] == choice2 ].sort_values( '가격(\)', ascending=False ) )
    

    
       
    
