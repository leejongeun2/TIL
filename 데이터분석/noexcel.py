import pandas as pd
from glob import glob
from tqdm.notebook import tqdm # 프로그레스바
import os

# temp = pd.read_excel("./data/opinet/지역_위치별(주유소) (1).xls")
# print(temp)

stations_files = glob('./data/opinet/*.xls')
# print(len(stations_files)) # 모든 파일 다 가져옴 41개

# temp = pd.read_excel(stations_files[0], header=2)
# temp2 = pd.read_excel(stations_files[1], header=2)
# print(pd.concat([temp, temp2]))

total = pd.DataFrame()
for file_name in stations_files:
    temp = pd.read_excel(file_name, header=2)
    total = pd.concat([total, temp])

total = total.sort_values(by="지역")
total = total.reset_index(drop=True) # 기존 인덱스를 날림

save_total = total.to_excel("전체주유소_가격.xlsx", index=False) # 앞에 인덱스컬럼 삭제
print(save_total)
    