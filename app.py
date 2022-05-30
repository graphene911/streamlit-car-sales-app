import streamlit as st
from app_eda import run_eda
from app_home import run_home
from app_ml import run_ml
from app_upload import run_upload
from PIL import Image




def main() :

    st.set_page_config(layout="wide")

    

    menu = ['Home', 'EDA', 'ML', 'UPLOAD']
    choice = st.sidebar.selectbox('메뉴 선택', menu)

    if choice == menu[0] :
        run_home()
    elif choice == menu[1] :
        run_eda()
    elif choice == menu[2] :
        run_ml()
    elif choice == menu[3] :
        run_upload()








if __name__ == '__main__' :
    main()