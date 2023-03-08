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
print(columns2)
