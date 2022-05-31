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


    maker_df = list(df['제조사명'].unique())
    choice = st.sidebar.selectbox('브랜드 선택', maker_df)
    user = st.sidebar.text_input('모델 검색')
    result = df.loc[ df['모델'].str.lower().str.contains(user.lower()),]

    if choice == maker_df[0] :
        st.write('Ford')
        ford_df = df.groupby('제조사명').get_group('Ford')
        st.dataframe(ford_df.loc[ ford_df['모델'].str.lower().str.contains(user.lower()),].sort_values('가격(\)', ascending=False))
    if choice == maker_df[1] :
        st.write('Dodge')
        ford_df = df.groupby('제조사명').get_group('Dodge')
        st.dataframe(ford_df.loc[ ford_df['모델'].str.lower().str.contains(user.lower()),].sort_values('가격(\)', ascending=False))
    if choice == maker_df[2] :
        st.write('Mazda')
        ford_df = df.groupby('제조사명').get_group('Mazda')
        st.dataframe(ford_df.loc[ ford_df['모델'].str.lower().str.contains(user.lower()),].sort_values('가격(\)', ascending=False))
    if choice == maker_df[3] :
        st.write('Audi')
        ford_df = df.groupby('제조사명').get_group('Audi')
        st.dataframe(ford_df.loc[ ford_df['모델'].str.lower().str.contains(user.lower()),].sort_values('가격(\)', ascending=False))
    if choice == maker_df[4] :
        st.write('Volkswagen')
        ford_df = df.groupby('제조사명').get_group('Volkswagen')
        st.dataframe(ford_df.loc[ ford_df['모델'].str.lower().str.contains(user.lower()),].sort_values('가격(\)', ascending=False))
    if choice == maker_df[5] :
        st.write('Opel')
        ford_df = df.groupby('제조사명').get_group('Opel')
        st.dataframe(ford_df.loc[ ford_df['모델'].str.lower().str.contains(user.lower()),].sort_values('가격(\)', ascending=False))
    if choice == maker_df[6] :
        st.write('Volvo')
        ford_df = df.groupby('제조사명').get_group('Volvo')
        st.dataframe(ford_df.loc[ ford_df['모델'].str.lower().str.contains(user.lower()),].sort_values('가격(\)', ascending=False))
    if choice == maker_df[7] :
        st.write('Peugeot')
        ford_df = df.groupby('제조사명').get_group('Peugeot')
        st.dataframe(ford_df.loc[ ford_df['모델'].str.lower().str.contains(user.lower()),].sort_values('가격(\)', ascending=False))
    if choice == maker_df[8] :
        st.write('Renault')
        ford_df = df.groupby('제조사명').get_group('Renault')
        st.dataframe(ford_df.loc[ ford_df['모델'].str.lower().str.contains(user.lower()),].sort_values('가격(\)', ascending=False))
    if choice == maker_df[9] :
        st.write('Honda')
        ford_df = df.groupby('제조사명').get_group('Honda')
        st.dataframe(ford_df.loc[ ford_df['모델'].str.lower().str.contains(user.lower()),].sort_values('가격(\)', ascending=False))
    if choice == maker_df[10] :
        st.write('Toyota')
        ford_df = df.groupby('제조사명').get_group('Toyota')
        st.dataframe(ford_df.loc[ ford_df['모델'].str.lower().str.contains(user.lower()),].sort_values('가격(\)', ascending=False))
    if choice == maker_df[11] :
        st.write('Mercedes-Benz')
        ford_df = df.groupby('제조사명').get_group('Mercedes-Benz')
        st.dataframe(ford_df.loc[ ford_df['모델'].str.lower().str.contains(user.lower()),].sort_values('가격(\)', ascending=False))
    if choice == maker_df[12] :
        st.write('Citroen')
        ford_df = df.groupby('제조사명').get_group('Citroen')
        st.dataframe(ford_df.loc[ ford_df['모델'].str.lower().str.contains(user.lower()),].sort_values('가격(\)', ascending=False))
    if choice == maker_df[13] :
        st.write('Hyundai')
        ford_df = df.groupby('제조사명').get_group('Hyundai')
        st.dataframe(ford_df.loc[ ford_df['모델'].str.lower().str.contains(user.lower()),].sort_values('가격(\)', ascending=False))
    if choice == maker_df[14] :
        st.write('ВАЗ')
        ford_df = df.groupby('제조사명').get_group('ВАЗ')
        st.dataframe(ford_df.loc[ ford_df['모델'].str.lower().str.contains(user.lower()),].sort_values('가격(\)', ascending=False))
    if choice == maker_df[15] :
        st.write('Skoda')
        ford_df = df.groupby('제조사명').get_group('Skoda')
        st.dataframe(ford_df.loc[ ford_df['모델'].str.lower().str.contains(user.lower()),].sort_values('가격(\)', ascending=False))
    if choice == maker_df[16] :
        st.write('BMW')
        ford_df = df.groupby('제조사명').get_group('BMW')
        st.dataframe(ford_df.loc[ ford_df['모델'].str.lower().str.contains(user.lower()),].sort_values('가격(\)', ascending=False))
    if choice == maker_df[17] :
        st.write('Kia')
        ford_df = df.groupby('제조사명').get_group('Kia')
        st.dataframe(ford_df.loc[ ford_df['모델'].str.lower().str.contains(user.lower()),].sort_values('가격(\)', ascending=False))
    if choice == maker_df[18] :
        st.write('Fiat')
        ford_df = df.groupby('제조사명').get_group('Fiat')
        st.dataframe(ford_df.loc[ ford_df['모델'].str.lower().str.contains(user.lower()),].sort_values('가격(\)', ascending=False))
    if choice == maker_df[19] :
        st.write('Chrysler')
        ford_df = df.groupby('제조사명').get_group('Chrysler')
        st.dataframe(ford_df.loc[ ford_df['모델'].str.lower().str.contains(user.lower()),].sort_values('가격(\)', ascending=False))
    if choice == maker_df[20] :
        st.write('Mitsubishi')
        ford_df = df.groupby('제조사명').get_group('Mitsubishi')
        st.dataframe(ford_df.loc[ ford_df['모델'].str.lower().str.contains(user.lower()),].sort_values('가격(\)', ascending=False))
    if choice == maker_df[21] :
        st.write('Rover')
        ford_df = df.groupby('제조사명').get_group('Rover')
        st.dataframe(ford_df.loc[ ford_df['모델'].str.lower().str.contains(user.lower()),].sort_values('가격(\)', ascending=False))
    if choice == maker_df[22] :
        st.write('Chevrolet')
        ford_df = df.groupby('제조사명').get_group('Chevrolet')
        st.dataframe(ford_df.loc[ ford_df['모델'].str.lower().str.contains(user.lower()),].sort_values('가격(\)', ascending=False))
    if choice == maker_df[23] :
        st.write('Nissan')
        ford_df = df.groupby('제조사명').get_group('Nissan')
        st.dataframe(ford_df.loc[ ford_df['모델'].str.lower().str.contains(user.lower()),].sort_values('가격(\)', ascending=False))
    if choice == maker_df[24] :
        st.write('Lifan')
        ford_df = df.groupby('제조사명').get_group('Lifan')
        st.dataframe(ford_df.loc[ ford_df['모델'].str.lower().str.contains(user.lower()),].sort_values('가격(\)', ascending=False))
    if choice == maker_df[25] :
        st.write('LADA')
        ford_df = df.groupby('제조사명').get_group('LADA')
        st.dataframe(ford_df.loc[ ford_df['모델'].str.lower().str.contains(user.lower()),].sort_values('가격(\)', ascending=False))
    if choice == maker_df[26] :
        st.write('Jaguar')
        ford_df = df.groupby('제조사명').get_group('Jaguar')
        st.dataframe(ford_df.loc[ ford_df['모델'].str.lower().str.contains(user.lower()),].sort_values('가격(\)', ascending=False))
    if choice == maker_df[27] :
        st.write('УАЗ')
        ford_df = df.groupby('제조사명').get_group('УАЗ')
        st.dataframe(ford_df.loc[ ford_df['모델'].str.lower().str.contains(user.lower()),].sort_values('가격(\)', ascending=False))
    if choice == maker_df[28] :
        st.write('Seat')
        ford_df = df.groupby('제조사명').get_group('Seat')
        st.dataframe(ford_df.loc[ ford_df['모델'].str.lower().str.contains(user.lower()),].sort_values('가격(\)', ascending=False))
    if choice == maker_df[29] :
        st.write('Buick')
        ford_df = df.groupby('제조사명').get_group('Buick')
        st.dataframe(ford_df.loc[ ford_df['모델'].str.lower().str.contains(user.lower()),].sort_values('가격(\)', ascending=False))
    if choice == maker_df[30] :
        st.write('Land Rover')
        ford_df = df.groupby('제조사명').get_group('Land Rover')
        st.dataframe(ford_df.loc[ ford_df['모델'].str.lower().str.contains(user.lower()),].sort_values('가격(\)', ascending=False))
    if choice == maker_df[31] :
        st.write('Porsche')
        ford_df = df.groupby('제조사명').get_group('Porsche')
        st.dataframe(ford_df.loc[ ford_df['모델'].str.lower().str.contains(user.lower()),].sort_values('가격(\)', ascending=False))
    if choice == maker_df[32] :
        st.write('Suzuki')
        ford_df = df.groupby('제조사명').get_group('Suzuki')
        st.dataframe(ford_df.loc[ ford_df['모델'].str.lower().str.contains(user.lower()),].sort_values('가격(\)', ascending=False))
    if choice == maker_df[33] :
        st.write('Alfa Romeo')
        ford_df = df.groupby('제조사명').get_group('Alfa Romeo')
        st.dataframe(ford_df.loc[ ford_df['모델'].str.lower().str.contains(user.lower()),].sort_values('가격(\)', ascending=False))
    if choice == maker_df[34] :
        st.write('Daewoo')
        ford_df = df.groupby('제조사명').get_group('Daewoo')
        st.dataframe(ford_df.loc[ ford_df['모델'].str.lower().str.contains(user.lower()),].sort_values('가격(\)', ascending=False))
    if choice == maker_df[35] :
        st.write('Mini')
        ford_df = df.groupby('제조사명').get_group('Mini')
        st.dataframe(ford_df.loc[ ford_df['모델'].str.lower().str.contains(user.lower()),].sort_values('가격(\)', ascending=False))
    if choice == maker_df[36] :
        st.write('Subaru')
        ford_df = df.groupby('제조사명').get_group('Subaru')
        st.dataframe(ford_df.loc[ ford_df['모델'].str.lower().str.contains(user.lower()),].sort_values('가격(\)', ascending=False))
    if choice == maker_df[37] :
        st.write('Lexus')
        ford_df = df.groupby('제조사명').get_group('Lexus')
        st.dataframe(ford_df.loc[ ford_df['모델'].str.lower().str.contains(user.lower()),].sort_values('가격(\)', ascending=False))
    if choice == maker_df[38] :
        st.write('Saab')
        ford_df = df.groupby('제조사명').get_group('Saab')
        st.dataframe(ford_df.loc[ ford_df['모델'].str.lower().str.contains(user.lower()),].sort_values('가격(\)', ascending=False))
    if choice == maker_df[39] :
        st.write('ГАЗ')
        ford_df = df.groupby('제조사명').get_group('ГАЗ')
        st.dataframe(ford_df.loc[ ford_df['모델'].str.lower().str.contains(user.lower()),].sort_values('가격(\)', ascending=False))
    if choice == maker_df[40] :
        st.write('Lancia')
        ford_df = df.groupby('제조사명').get_group('Lancia')
        st.dataframe(ford_df.loc[ ford_df['모델'].str.lower().str.contains(user.lower()),].sort_values('가격(\)', ascending=False))
    if choice == maker_df[41] :
        st.write('Pontiac')
        ford_df = df.groupby('제조사명').get_group('Pontiac')
        st.dataframe(ford_df.loc[ ford_df['모델'].str.lower().str.contains(user.lower()),].sort_values('가격(\)', ascending=False))
    if choice == maker_df[42] :
        st.write('Geely')
        ford_df = df.groupby('제조사명').get_group('Geely')
        st.dataframe(ford_df.loc[ ford_df['모델'].str.lower().str.contains(user.lower()),].sort_values('가격(\)', ascending=False))
    if choice == maker_df[43] :
        st.write('Acura')
        ford_df = df.groupby('제조사명').get_group('Acura')
        st.dataframe(ford_df.loc[ ford_df['모델'].str.lower().str.contains(user.lower()),].sort_values('가격(\)', ascending=False))
    if choice == maker_df[44] :
        st.write('Jeep')
        ford_df = df.groupby('제조사명').get_group('Jeep')
        st.dataframe(ford_df.loc[ ford_df['모델'].str.lower().str.contains(user.lower()),].sort_values('가격(\)', ascending=False))
    if choice == maker_df[45] :
        st.write('Chery')
        ford_df = df.groupby('제조사명').get_group('Chery')
        st.dataframe(ford_df.loc[ ford_df['모델'].str.lower().str.contains(user.lower()),].sort_values('가격(\)', ascending=False))
    if choice == maker_df[46] :
        st.write('Infiniti')
        ford_df = df.groupby('제조사명').get_group('Infiniti')
        st.dataframe(ford_df.loc[ ford_df['모델'].str.lower().str.contains(user.lower()),].sort_values('가격(\)', ascending=False))
    if choice == maker_df[47] :
        st.write('SsangYong')
        ford_df = df.groupby('제조사명').get_group('SsangYong')
        st.dataframe(ford_df.loc[ ford_df['모델'].str.lower().str.contains(user.lower()),].sort_values('가격(\)', ascending=False))
    if choice == maker_df[48] :
        st.write('Dacia')
        ford_df = df.groupby('제조사명').get_group('Dacia')
        st.dataframe(ford_df.loc[ ford_df['모델'].str.lower().str.contains(user.lower()),].sort_values('가격(\)', ascending=False))
    if choice == maker_df[49] :
        st.write('ЗАЗ')
        ford_df = df.groupby('제조사명').get_group('ЗАЗ')
        st.dataframe(ford_df.loc[ ford_df['모델'].str.lower().str.contains(user.lower()),].sort_values('가격(\)', ascending=False))
    if choice == maker_df[50] :
        st.write('Great Wall')
        ford_df = df.groupby('제조사명').get_group('Great Wall')
        st.dataframe(ford_df.loc[ ford_df['모델'].str.lower().str.contains(user.lower()),].sort_values('가격(\)', ascending=False))
    if choice == maker_df[51] :
        st.write('Lincoln')
        ford_df = df.groupby('제조사명').get_group('Lincoln')
        st.dataframe(ford_df.loc[ ford_df['모델'].str.lower().str.contains(user.lower()),].sort_values('가격(\)', ascending=False))
    if choice == maker_df[52] :
        st.write('Cadillac')
        ford_df = df.groupby('제조사명').get_group('Cadillac')
        st.dataframe(ford_df.loc[ ford_df['모델'].str.lower().str.contains(user.lower()),].sort_values('가격(\)', ascending=False))
    if choice == maker_df[53] :
        st.write('Iveco')
        ford_df = df.groupby('제조사명').get_group('Iveco')
        st.dataframe(ford_df.loc[ ford_df['모델'].str.lower().str.contains(user.lower()),].sort_values('가격(\)', ascending=False))
    if choice == maker_df[54] :
        st.write('Москвич')
        ford_df = df.groupby('제조사명').get_group('Москвич')
        st.dataframe(ford_df.loc[ ford_df['모델'].str.lower().str.contains(user.lower()),].sort_values('가격(\)', ascending=False))
    
    
    
        

        

        