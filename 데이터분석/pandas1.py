import numpy as np # 수치연산
import pandas as pd
import matplotlib.pyplot as plt # 그래프
import seaborn as sns # 그래프

# 데이터 프레임은 테이블이고, 한줄한줄이 시리즈(로우 또는 컬럼)

# s는 1, 3, 5, 6, 8을 원소로가지는 pandas.Series, 시리즈는 하나의 데이터 타입
first = pd.Series([1, 3, 5, 6, 8])
# print(first)

# 12*4 행렬에서 1부터 48까지의 숫자 원소를 가지고, index는 0부터 시작하고, 순서대로 x1...
df = pd.DataFrame(data=np.arange(1, 49).reshape(12, 4), columns=["X1", "X2", "X3", "X4"])
# print(df)

# 특정 컬럼 가져오기
columns1 = df["X1"]
# print(columns1)

# x1컬럼에 2를 더하기
columns1plus = df["X1"] + 2 # 더하는 게 각 원소에 뿌려짐(for문 돌 필요가 없음)
# print(columns1plus)

# 맨 위 다섯줄 보여주는 함수
df.head()

# 10줄
df.head(10)

# 전체적인 요약정보
df.info()

# 전체적인 통계정보 => 컬럼 단위 기준
df.describe()

# x2 컬럼을 기준으로 내림차순 정렬
columns2 = df.sort_values(by="X2", ascending=False)
# print(columns2)

# 컬럼 자체
df["X1"]

# 데이터프레임 3줄 슬라이싱(행)
df[0:3]

# 인덱스 밸류 기준으로 인덱싱
df.loc[0] # 행기준 인덱스에 해당하는 로우가 나옴, 리스트의 인덱싱과 다름, 더 큰 개념

# df.loc는 특정 값 기준으로 인덱싱(특정 원소)
df.loc[0][2]
df.loc[0]["X3"]

# 가장 중요!! df.locdp 이차원 인덱싱, df.loc["row에 대한 조건", "col에 대한 조건"] 행조건, 열조건
df.loc[4, "X2"]
df.loc[[0, 3], ["X1", 'X3']]
df.loc[0:4, "X1":"X3"] # loc로 슬라이싱하면 모든 범위가 포함됨!!

# x1에서 10보다 큰 값을 가지고 있는 모든 로우 출력하고 싶을 때 

mask = df["X1"] > 10 # TRUE, FALSE로 나옴, raw에 대한 조건
result = df.loc[mask]
# print(result)

# df에서 x2컬럼이 20이상인 모든 데이터(row)를 출력하세요. 

result1 = df.loc[df["X2"] >= 20] # 바로 적는 것도 가능
# print(result1)

# df에서 x2컬럼이 20이상인 x4를 출력하세요. 
df.loc[df["X2"] >= 20, "X4"]

# x3컬럼에서 10이상, 30이하인 데이터 뽑아주세요.
mask3 = (10 <= df["X3"]) & (df["X3"] <= 30) # 위 아래 붙여서 쓰면 에러가남, 두개로 찢어야함
df.loc[(10 <= df["X3"]) & (df["X3"] <= 30)]

# x2컬럼에서 10보다 작거나, 30보다 큰 데이터를 뽑아주세요.
#| 활용
mask4 = (10 > df["X2"]) | (df["X2"] > 30)
result2 = df.loc[mask4]
print(result2)

# 3번째 row부터 8번째 row까지, 첫번째 컬럼부터 3개
df.iloc[2:8, 0:3] # 위치정보로 봅을 수 있음(조건은 안됨)






