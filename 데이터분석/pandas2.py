import numpy as np # 수치연산
import pandas as pd
import matplotlib.pyplot as plt # 그래프
import seaborn as sns # 그래프

titanic = pd.read_csv("./titanic.csv") # /가 어떤 폴더 안에 있다는 뜻, 891행, 12개 컬럼
# print(titanic) 

# age가 30이상인 사람들의 이름
age30 = titanic.loc[titanic["Age"] >= 30, "Name"]
# print(age30)

# 성별을 기준으로 생존률 파악 --> mean vs sum, 기준으로 재구성해서 쓰는 것이기 때문에 피벗테이블을 사용
sex_survive = pd.pivot_table(data=titanic, index="Sex", values="Survived", aggfunc=["mean", "sum", "count"]) # mean(평균, 생존률)
# print(sex_survive)

# 사회 계급을 기준으로 생존률 파악
pclass_survive = pd.pivot_table(data=titanic, index=["Pclass", "Sex"], values="Survived", aggfunc=["count", "sum", "mean"] )
print(pclass_survive)
