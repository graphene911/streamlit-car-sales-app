import streamlit as st
import pandas as pd
from PIL import Image


def run_serch() :

    img2 = Image.open('data/img2.jpg')
    st.sidebar.image(img2, width=297)

    st.title('차량 검색')

    df = pd.read_csv('data/car_price_sales.csv', index_col=0)
    df = df.iloc[:,:-1]


    df1 = sorted(list(df['제조사명'].unique()))
    choice = st.sidebar.selectbox('브랜드 선택', df1)
    serch_type = ['모델','타입']
    serch_type_df = st.sidebar.selectbox('모델/타입 선택',serch_type)
    
    #### 브랜드별 이미지 ####
    if choice == df1[0] :
        img0 = Image.open('data/logo/000.jpg')
        st.image(img0)
    elif choice == df1[1] :
        img1 = Image.open('data/logo/001.jpg')
        st.image(img1)
    elif choice == df1[2] :
        img2 = Image.open('data/logo/002.jpg')
        st.image(img2)
    elif choice == df1[3] :
        img3 = Image.open('data/logo/003.jpg')
        st.image(img3)
    elif choice == df1[4] :
        img4 = Image.open('data/logo/004.jpg')
        st.image(img4)
    elif choice == df1[5] :
        img5 = Image.open('data/logo/005.jpg')
        st.image(img5)
    elif choice == df1[6] :
        img6 = Image.open('data/logo/006.jpg')
        st.image(img6)
    elif choice == df1[7] :
        img7 = Image.open('data/logo/007.jpg')
        st.image(img7)
    elif choice == df1[8] :
        img8 = Image.open('data/logo/008.jpg')
        st.image(img8)
    elif choice == df1[9] :
        img9 = Image.open('data/logo/009.jpg')
        st.image(img9)
    elif choice == df1[10] :
        img10 = Image.open('data/logo/010.jpg')
        st.image(img10)
    elif choice == df1[11] :
        img11 = Image.open('data/logo/011.jpg')
        st.image(img11)
    elif choice == df1[12] :
        img12 = Image.open('data/logo/012.jpg')
        st.image(img12)
    elif choice == df1[13] :
        img13 = Image.open('data/logo/013.jpg')
        st.image(img13)
    elif choice == df1[14] :
        img14 = Image.open('data/logo/014.jpg')
        st.image(img14)
    elif choice == df1[15] :
        img15 = Image.open('data/logo/015.jpg')
        st.image(img15)
    elif choice == df1[16] :
        img16 = Image.open('data/logo/016.jpg')
        st.image(img16)
    elif choice == df1[17] :
        img17 = Image.open('data/logo/017.jpg')
        st.image(img17)
    elif choice == df1[18] :
        img18 = Image.open('data/logo/018.jpg')
        st.image(img18)
    elif choice == df1[19] :
        img19 = Image.open('data/logo/019.jpg')
        st.image(img19)
    elif choice == df1[20] :
        img20 = Image.open('data/logo/020.jpg')
        st.image(img20)
    elif choice == df1[21] :
        img21 = Image.open('data/logo/021.jpg')
        st.image(img21)
    elif choice == df1[22] :
        img22 = Image.open('data/logo/022.jpg')
        st.image(img22)
    elif choice == df1[23] :
        img23 = Image.open('data/logo/023.jpg')
        st.image(img23)
    elif choice == df1[24] :
        img24 = Image.open('data/logo/024.jpg')
        st.image(img24)
    elif choice == df1[25] :
        img25 = Image.open('data/logo/025.jpg')
        st.image(img25)
    elif choice == df1[26] :
        img26 = Image.open('data/logo/026.jpg')
        st.image(img26)
    elif choice == df1[27] :
        img27 = Image.open('data/logo/027.jpg')
        st.image(img27)
    elif choice == df1[28] :
        img28 = Image.open('data/logo/028.jpg')
        st.image(img28)
    elif choice == df1[29] :
        img29 = Image.open('data/logo/029.jpg')
        st.image(img29)
    elif choice == df1[30] :
        img30 = Image.open('data/logo/030.jpg')
        st.image(img30)
    elif choice == df1[31] :
        img31 = Image.open('data/logo/031.jpg')
        st.image(img31)
    elif choice == df1[32] :
        img32 = Image.open('data/logo/032.jpg')
        st.image(img32)
    elif choice == df1[33] :
        img33 = Image.open('data/logo/033.jpg')
        st.image(img33)
    elif choice == df1[34] :
        img34 = Image.open('data/logo/034.jpg')
        st.image(img34)
    elif choice == df1[35] :
        img35 = Image.open('data/logo/035.jpg')
        st.image(img35)
    elif choice == df1[36] :
        img36 = Image.open('data/logo/036.jpg')
        st.image(img36)
    elif choice == df1[37] :
        img37 = Image.open('data/logo/037.jpg')
        st.image(img37)
    elif choice == df1[38] :
        img38 = Image.open('data/logo/038.jpg')
        st.image(img38)
    elif choice == df1[39] :
        img39 = Image.open('data/logo/039.jpg')
        st.image(img39)
    elif choice == df1[40] :
        img40 = Image.open('data/logo/040.jpg')
        st.image(img40)
    elif choice == df1[41] :
        img41 = Image.open('data/logo/041.jpg')
        st.image(img41)
    elif choice == df1[42] :
        img42 = Image.open('data/logo/042.jpg')
        st.image(img42)
    elif choice == df1[43] :
        img43 = Image.open('data/logo/043.jpg')
        st.image(img43)
    elif choice == df1[44] :
        img44 = Image.open('data/logo/044.jpg')
        st.image(img44)
    elif choice == df1[45] :
        img45 = Image.open('data/logo/045.jpg')
        st.image(img45)
    elif choice == df1[46] :
        img46 = Image.open('data/logo/046.jpg')
        st.image(img46)
    elif choice == df1[47] :
        img47 = Image.open('data/logo/047.jpg')
        st.image(img47)
    elif choice == df1[48] :
        img48 = Image.open('data/logo/048.jpg')
        st.image(img48)
    elif choice == df1[49] :
        img49 = Image.open('data/logo/049.jpg')
        st.image(img49)
    elif choice == df1[50] :
        img50 = Image.open('data/logo/050.jpg')
        st.image(img50)
    elif choice == df1[51] :
        img51 = Image.open('data/logo/051.jpg')
        st.image(img51)
    elif choice == df1[52] :
        img52 = Image.open('data/logo/052.jpg')
        st.image(img52)
    elif choice == df1[53] :
        img53 = Image.open('data/logo/053.jpg')
        st.image(img53)
    elif choice == df1[54] :
        img54 = Image.open('data/logo/054.jpg')
        st.image(img54)

    #### 모델별 타입별 selectbox ####
    if serch_type_df == serch_type[0] :
        df2 = df.groupby('제조사명').get_group(choice)
        df2_list = sorted(df2['모델'].unique())
        choice2 = st.sidebar.selectbox('모델 선택', df2_list)
        st.subheader('모델별 보기')
        st.dataframe( df2.loc[ df2['모델'] == choice2 ].sort_values( '가격(\)', ascending=False ) )
    
    if serch_type_df == serch_type[1] :
        df3 = df.groupby('제조사명').get_group(choice)
        df3_list = sorted(df3['타입'].unique())
        choice3 = st.sidebar.selectbox('타입 선택', df3_list)
        st.subheader('타입별 보기')
        st.dataframe( df3.loc[ df3['타입'] == choice3 ].sort_values( '가격(\)', ascending=False ) )

    
       
    
