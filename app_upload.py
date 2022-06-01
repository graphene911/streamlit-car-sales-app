import streamlit as st
import pandas as pd
from PIL import Image
import os
from datetime import datetime
from PIL import Image


## 파일 업로드 함수 ##

def save_uploaded_file(directory, file) :
    # 1.디렉토리가 있는지 확인하여, 없으면 디렉토리부터만든다.
    if not os.path.exists(directory) :
        os.makedirs(directory)
    # 2. 디렉토리가 있으니, 파일을 저장.
    with open(os.path.join(directory, file.name), 'wb') as f :
        f.write(file.getbuffer())
    return st.success("Saved file : {} in {}".format(file.name, directory))

def run_upload() :
    st.title('여러 파일 한번에 업로드하는 앱')
    
    img5 = Image.open('data\img6.jpg')
    st.sidebar.image(img5, width=297)

    # 사이드바 메뉴
    menu = ['차량등록', '파일등록']
    choice = st.sidebar.selectbox( 'menu', menu )

    # accept_multiple_files=True을 셋팅하면 여러 파일들을 한꺼번에 받을 수 있다.

    if choice == menu[0]:
        df = pd.read_csv('data/car_price_sales.csv', index_col=0)

        brand_type = ['Ford', 'Dodge', 'Mazda', 'Audi', 'Volkswagen', 'Opel', 'Volvo', 'Peugeot', 'Renault', 'Honda', 'Toyota', 'Mercedes-Benz',
        'Citroen', 'Hyundai', 'ВАЗ', 'Skoda', 'BMW', 'Kia', 'Fiat', 'Chrysler', 'Mitsubishi', 'Rover', 'Chevrolet', 'Nissan', 'Lifan','LADA',
        'Jaguar', 'УАЗ', 'Seat', 'Buick', 'Land Rover', 'Porsche', 'Suzuki', 'Alfa Romeo', 'Daewoo', 'Mini', 'Subaru', 'Lexus','Saab', 'ГАЗ',
        'Lancia', 'Pontiac', 'Geely', 'Acura', 'Jeep', 'Chery', 'Infiniti', 'SsangYong', 'Dacia', 'ЗАЗ', 'Great Wall','Lincoln', 'Cadillac', 'Iveco', 'Москвич']
        brand_text = st.selectbox('제조사', brand_type)
        model_text = st.text_input('모델')
        trans_type = ['mechanical', 'automatic']
        trans_text = st.selectbox('변속기 유형', trans_type)
        color_text = st.text_input('색상')
        km_text = st.number_input('주행거리(km)')
        year_text = st.number_input('연식')
        oil_type = ['gasoline', 'diesel', 'gas', 'hybrid-petrol', 'electric', 'hybrid-diesel']
        oil_text = st.selectbox('연료',oil_type)
        cc_text = st.number_input('배기량')
        car_type = ['hatchback', 'minivan', 'universal', 'sedan', 'van', 'suv', 'pickup', 'liftback', 'minibus', 'coupe', 'cabriolet', 'limousine']
        type_text = st.selectbox('차량 타입', car_type)
        wa_text = st.radio('보증기간 유/무', ['True','False'])
        if wa_text == 'False' :
            wa_text = 0 
        else :
            wa_text = 1
        fr_type = ['front', 'rear', 'all']
        fr_text = st.selectbox('구동방식', fr_type)
        price_text = st.number_input('가격')

        new_car = [{'제조사명' : brand_text , '모델' : model_text, '변속기유형' : trans_text, '색상' : color_text, '주행거리(km)' : km_text,
        '연식' : year_text, '연료' : oil_text, '배기량' : cc_text, '타입' : type_text, '보증기간' : wa_text , '구동' : fr_text, '가격(\) ' : price_text}]
        new_car_df = pd.DataFrame(data = new_car)

        
        
        if st.button('차량 등록') :
            df = df.append(new_car_df,ignore_index=True)
            st.dataframe(df.sort_index(ascending=False))

    elif choice == menu[1] :
                
        upload_files = st.file_uploader('이미지 파일을 선택', type=['jpg', 'png', 'jpeg','csv'], accept_multiple_files=True)
    
        # upload_files는 여러파일들을 저장하고 있는 리스트
        # 업로드한 파일이 있는 경우에만, 아래 코드를 실행해야 한다.
        if upload_files is not None :
        
            # 업로드한 파일이 리스트이니깐, 하나씩 가져와서
            # temp 폴더에 저장할 것이다.
            for file in upload_files :
            
            # 파일명을 유니크하게 만들어서 저장
            # 현재시간을 활용해서, 파일명을 만든다.
                current_time = datetime.now()         
                new_filename = current_time.isoformat().replace(':','_') + '.png'

                file.name = new_filename
                save_uploaded_file('temp',file)
            
            # 저장이 다 끝나면, 웹 브라우저에 이미지 표시
            for file in upload_files :
                img = Image.open(file)
                st. image(img)


    ## CSV 파일을 여러개 올리면, 이 파일들을 temp에 저장하고
    ## 데이터프레임으로 읽어서 화면에 표시