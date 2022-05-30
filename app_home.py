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
    st.dataframe(df)



    