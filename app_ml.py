import streamlit as st
import pandas as pd
import joblib
import numpy as np
import sklearn
from sklearn.linear_model import LinearRegression
from PIL import Image

def run_ml() :

    img4 = Image.open('data/img1.jpg')
    st.sidebar.image(img4, width=297)

    st.title('고객정보 입력으로 차량 구매가능 금액 예측 및 추천')

    st.subheader('차량 검색')
    df = pd.read_csv('data/car_price_sales.csv', index_col=0)

    word = st.text_input('검색할 모델명을 입력하세요')
    result = df.loc[ df['모델'].str.lower().str.contains(word.lower()),].sort_values(['제조사명','타입','가격(\)'])
    result = result.iloc[:,:-1]
    st.dataframe(result)

    st.subheader('고객 차량 구매금액 예측')

    regressor = joblib.load('data/regressor1.pkl')
    scaler_X = joblib.load('data/scaler_X1.pkl')
    scaler_y = joblib.load('data/scaler_y1.pkl')

    gender = st.sidebar.radio('성별 입력', ['남자','여자'])

    if gender == '여자' :
       gender = 0
    
    else :
        gender = 1

    age= st.sidebar. number_input('나이 입력',0,120)
    salary= st.sidebar. number_input('연봉 입력',0)
    debt= st.sidebar. number_input('카드빚 입력',0)
    worth= st.sidebar. number_input('자산 입력',0)

    if st.checkbox('자동차 구매 금액 예측') : 

        # 1. 신규 고객의 정보를 넘파이 어레이로 만들어준다.
        new_data = np.array([gender,age,salary,debt,worth])

        # 2. 학습할때 사용한 X 의 피처 스케일러를 이용해서, 피처스케일링하기
        # 먼저, 데이터를 2차원으로 만들어준다.
        new_data = new_data.reshape(1, 5)
        new_data = scaler_X.transform(new_data)

        # 3. 인공지능에게 예측해달라고 한다.
        y_pred = regressor.predict(new_data)
        
        # 4. 예측한 값을, 원상복구 시킨다.
        y_pred = scaler_y.inverse_transform(y_pred)

        y_pred = round(y_pred[0,0])
        
        st.sidebar.write('구매 가능 금액은 '  + str(y_pred) + '원 입니다.')
        st.write('구매 가능 금액은 '  + str(y_pred) + '원 입니다.')
        st.subheader('구매 가능한 차량 입니다.')
        suc_df = st.dataframe(df.loc[df['가격(\)'] < y_pred ].sort_values(['제조사명','타입','가격(\)'], ascending=False))



