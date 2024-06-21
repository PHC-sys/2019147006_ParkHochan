# 2019147006 박호찬_Final Project
## 프레젠테이션은 Presentation(Base Strategy Boosting with ML).pdf 로 업로드 했습니다.

### Abstract: 'Advances in Machine Learning'에 기반한 KOSDAQ 150 지수 데이터를 이용해 백테스팅 엔진 구현

1. Tick Data(High Frequency Data) 이용한 전처리 : 시간 단위로 나뉘어져 있는 가격 데이터 > 거래 금액/거래량 기준으로 재구성 (한 차트 바 데이터에 들어가는 정보량을 균등하게 맞춰주는 작업)
2. 1차 Base Model(Trading Strategy) 구축 : Price Momentum 강도를 판단할 지표와 이상치 구분을 위한 Parkinson Volatility 사용
3. 금융 데이터에 맞게 적당한 기법 사용 : Tripple Barrier(시계열적 상관성이 높은 금융 데이터를 다루는 일종의 기법) & Meta Labeling(시그널이 True Positive인지 False Positive인지에 대한 Binary Label)
4. 2차 Machine Learning Model 구축 : Random Forest 이용 > Base Model의 Signal의 True/False 여부 판단하는 모델


