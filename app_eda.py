from turtle import width
import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import platform
import matplotlib.font_manager as fm
from PIL import Image



############### 그래프에서 한국어 인식 ###############
import platform

from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
elif platform.system() == 'Linux':
    rc('font', family='NanumGothic')    
else:
    print('Unknown system')


def run_eda() :
    

    img3 = Image.open('data/img3.jpg')
    st.sidebar.image(img3, width=297)

    eda_list = st.sidebar.radio('성별 입력', ['차량 데이터','고객 데이터'])
        
    if eda_list == '차량 데이터':
        st.title('차량 데이터 EDA')
        df = pd.read_csv('data/car_price_sales.csv', index_col=0)
        df = df.iloc[:,:-1]
    
                
        radio_menu = ['전체 데이터', '통계치']
        selected = st.radio('선택', radio_menu,)

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

        st.subheader('각 연료별 차량의 대수')
        
        fig6 = plt.figure(figsize=(8,6))
        sb.countplot(data=df, x='연료')
        st.pyplot(fig6)

    elif eda_list == '고객 데이터':
        st.title('고객 데이터 EDA')

        df1 = pd.read_csv('data/Car_Purchasing_Data.csv' ,encoding='ISO-8859-1' )

        # 라디오 버튼을 이용해서, 데이터 프레임과, 통계치를 선택해서 보여줄 수 있도록 만든다.

        radio_menu = ['전체 데이터', '통계치']
        selected = st.radio('선택하세요', radio_menu)

        if selected == radio_menu[0] :
            st.dataframe(df1)
        elif selected == radio_menu[1] :
            st.dataframe(df1.describe())



        ## 컬럼명을 보여주고, 컬럼을 선택하면,
        ## 해당 컬럼의 최대값 데이터와, 최소값 데이터를 보여준다.


        col_list = df1.columns[4 : ]
        selected_col = st.selectbox('최대 최소 원하는 컬럼 선택', col_list)

        df1_max = df1.loc[df1[selected_col] == df1[selected_col].max(),]
        df1_min = df1.loc[df1[selected_col] == df1[selected_col].min(),]
        
        st.text('{}컬럼의 최대값에 해당하는 데이터 입니다.'.format(selected_col))
        st.dataframe(df1_max)
        st.text('{}컬럼의 최소값에 해당하는 데이터 입니다.'.format(selected_col))
        st.dataframe(df1_min)


        ## 유저가 선택한 컬럼들만, pairplot 그리고
        # 그 아래 상관계수를 보여준다.

        selected_list = st.multiselect('컬럼들 선택', col_list)

        # print(selected_list)

        if len(selected_list) > 1 :
            path = '/usr/share/fonts/truetype/nanum/NanumMyeongjo.ttf' 
            fontprop = fm.FontProperties(fname=path, size=18)

            fig1 = sb.pairplot(data=df1[selected_list], fontproperties=fontprop)
            st.pyplot(fig1)

        st.text('선택하신 컬럼끼리의 상관계수입니다.')
        st.dataframe(df1[selected_list].corr())

    
