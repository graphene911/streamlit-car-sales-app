![header](https://capsule-render.vercel.app/api?type=Waving&color=0:fc00ff,100:00dbde&height=220&section=header&text=The%20Purchase%20of%20a%20Used%20Car%20APP&fontSize=50&&fontColor=ffff&animation=fadeIn)
<br/>
### GRAPHENE911 :gem: <br/><br/>
[![GitHub Badge](https://img.shields.io/badge/GitHub-181717?style=flat&logo=GitHub&logoColor=white)](https://github.com/graphene911/)
[![Tistory Badge](https://img.shields.io/badge/TSTORY-555263?style=flat&logoColor=white)](https://story-jy.tistory.com/)
[![Gmail Badge](https://img.shields.io/badge/Gmail-D14836?style=flat&logo=Gmail&logoColor=white)](mailto:graphene9110@gmail.com)
<br/>

### Languages
![Python Badge](https://img.shields.io/badge/Python-3776AB?style=flat&logo=Python&logoColor=white)
<br/>
[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=graphene911&layout=compact&theme=tokyonight&langs_count=8)](https://github.com/anuraghazra/github-readme-stats)
<br/>
### Library
![NumPy Badge](https://img.shields.io/badge/NumPy-013243?style=flat&logo=NumPy&logoColor=white)
![pandas Badge](https://img.shields.io/badge/pandas-150458?style=flat&logo=pandas&logoColor=white)
![scikit-learn Badge](https://img.shields.io/badge/scikit-learn-F7931E?style=flat&logo=scikit-learn&logoColor=white)
![Streamlit Badge](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=Streamlit&logoColor=white)
![matplotlib.pyplot Badge](https://img.shields.io/badge/matplotlib.pyplot-F7931E?style=flat&logo=matplotlib.pyplot&logoColor=white)
![Seaborn Badge](https://img.shields.io/badge/Seaborn-232F3E?style=flat&logo=Seaborn&logoColor=white)
<br/>
### Tool
![Anaconda Badge](https://img.shields.io/badge/Anaconda-44A833?style=flat&logo=Anaconda&logoColor=white)
![Google Colab Badge](https://img.shields.io/badge/Google%20Colab-F9AB00?style=flat&logo=Google%20Colab&logoColor=white)
![Visual Studio Code Badge](https://img.shields.io/badge/Visual%20Studio%20Code-007ACC?style=flat&logo=Visual%20Studio%20Code&logoColor=white)
![Amazon AWS Badge](https://img.shields.io/badge/Amazon%20AWS-232F3E?style=flat&logo=Amazon%20AWS&logoColor=white)

<img src=https://user-images.githubusercontent.com/105832364/172322883-7d1d1120-8cac-409d-9d49-873df0cdc166.jpg width="855" height="400"/><br/>
  - 개요
    - 중고차 판매자가 고객의 구매 가능 금액 예측을 통해 고객에게 알맞는 중고차를 추천 할 수 있으며,<br/>
     차량의 입 출고 관리를 통해 판매자가 소유한 차량의 재고를 관리 할 수 있습니다.
  
  - MENU
    - HOME
    - 차량검색
    - EDA
    - 구매금액 예측 (ML)
    - UPLOAD

<br/>

## Datasets
  - 차량데이터 (30824 rows × 11 columns)
    - 제조사명
    - 모델
    - 변속기유형
    - 색상
    - 주행거리(km)
    - 연식
    - 연료
    - 배기량
    - 타입
    - 구동
    - 가격<br/>

  - 고객데이터 (500 rows × 9 columns)
    - Customer Name
    - Customer e-mail
    - Country
    - Gender
    - Age
    - Annual Salary
    - Credit Card Debt
    - Net Worth
    - Car Purchase Amount

## Machine Learning (data = 고객데이터 )
<img src=https://user-images.githubusercontent.com/105832364/172328303-3b43121c-b70e-4c4a-a195-2cee778565f3.jpg width="855" height="400"/><br/>
  - NaN 제거
  - 학습을 위해 X , y지정
  - 피처스케일링(scikit-learn MinMaxScaler 사용)
  - 학습을 위해, y 의 shape 을 변경 후 피처스케일링(scikit-learn MinMaxScaler 사용)
  - 트레이닝셋과 테스트셋으로 분리 (from sklearn.model_selection import train_test_split)
  - 리니어 리그레션으로 모델링하고 학습한 후 평가
<br/>

## URL
  - http://54.180.100.25:8501/


<br/>

## Reference
  - 차량 데이터 : https://www.kaggle.com/datasets/sivaakhilnukala/used-cars-price
  - 고객 데이터 : https://www.kaggle.com/code/martandsay/car-purchase-amount-prediction-neural-network/notebook
<br/>

![Footer](https://capsule-render.vercel.app/api?type=waving&color=0:fc00ff,100:00dbde&height=100&section=footer)
