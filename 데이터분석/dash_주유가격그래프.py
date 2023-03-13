import pandas as pd
import seaborn as sns

oil_prices = pd.read_excel('./data/전체주유소_가격.xlsx')
# print(oil_prices) # 782row


# 휘발유, 경유, 실내 등유의 히스토그램

# EDA 해보자! 하고싶은걸 실제로 구현해보자. 70%이상

# 1.지역별로 몇개의 주유소?
result = oil_prices["지역"].value_counts() # 지역별로 몇개씩 있는지?많은 것 부터 나옴
# print(result)

# 1-1. 서울 데이터 뽑기
seoul_oil = oil_prices.loc[oil_prices["지역"]=="서울특별시", ["고급휘발유", "휘발유", "경유", "실내등유"]] 
# print(seoul_oil)

# 없는 것들을 0으로 바꾸기. - > 0으로
seoul_oil.loc[seoul_oil["고급휘발유"] == "-", "고급휘발유"] = 0
seoul_oil.loc[seoul_oil["휘발유"] == "-", "휘발유"] = 0
seoul_oil.loc[seoul_oil["경유"] == "-", "경유"] = 0
seoul_oil.loc[seoul_oil["실내등유"] == "-", "실내등유"] = 0

seoul_oil["고급휘발유"] = seoul_oil["고급휘발유"].astype('int')
seoul_oil["휘발유"] = seoul_oil["휘발유"].astype('int')
seoul_oil["경유"] = seoul_oil["경유"].astype('int')
seoul_oil["실내등유"] = seoul_oil["실내등유"].astype('int')
# result1 = seoul_oil.info()

df = seoul_oil.mean().reset_index() # 시리즈가 데이터프레임이 되는 함수
df.columns = ["oil type", "average prices"]
df["oil type"] = ["highend", "normal", "light", "inside"]
result1 = sns.barplot(data=df, x="oil type", y="average prices", palette="Set2")
# print(result1)

seoul_oil.columns = ["highend", "normal", "light", "inside"]
result_histplot = sns.histplot(data="seoul_oil", x="normal", bins=30)
result_scatterplot =sns.scatterplot(data=seoul_oil, x="normal", y="highend", ci=None)
print(result_scatterplot)