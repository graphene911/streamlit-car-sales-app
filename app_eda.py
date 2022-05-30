import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import platform

# 차트 한글 깨짐 방지 코드
from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system... sorry~~~~')


def run_eda() :

    st.title('재고차량 데이터 EDA')
    
    df = pd.read_csv('data/car_price_sales.csv', index_col=0)
    
    radio_menu = ['전체 데이터', '통계치']
    selected = st.radio('선택', radio_menu)

    if selected == radio_menu[0] :
        st.dataframe(df)
    elif selected == radio_menu[1] :
        st.dataframe(df.describe())

    st.title('')
    st.subheader('최대 최소값 분석')
    col_list = df.columns[4 : ]
    selected_col = st.selectbox('최대 최소 원하는 컬럼 선택', col_list)

    df_max = df.loc[df[selected_col] == df[selected_col].max(),]
    df_min = df.loc[df[selected_col] == df[selected_col].min(),]
    
    st.text('{}컬럼의 최대값에 해당하는 데이터 입니다.'.format(selected_col))
    st.dataframe(df_max)
    st.text('{}컬럼의 최소값에 해당하는 데이터 입니다.'.format(selected_col))
    st.dataframe(df_min)
    
    st.title('')
    st.subheader('상관계수분석')

    selected_list = st.multiselect('컬럼들 선택', col_list)
    if len(selected_list) > 1 :
        fig1 = sb.pairplot(data=df[selected_list])
        st.pyplot(fig1)
    
    st.text('선택하신 컬럼끼리의 상관계수입니다.')
    st.dataframe(df[selected_list].corr())