import pandas as pd
from time import time

# 1. 데이터 일부만 가져오기
# start = time()
part = pd.read_csv('./data/transactions_train.csv', nrows=1000) # 1000개만 불러오기
# end = time()
# print(end-start)
# print(part)


# 2. 일부 컬럼 뽑기
part2 = pd.read_csv('./data/transactions_train.csv', usecols=['t_dat', 'sales_channel_id']) # 31788324행
# Check memory usage => 용량
# mem_usage = part2.memory_usage(deep=True).sum() / 1024 / 1024 / 1024
# print(f"Memory Usage : {mem_usage:.4} GiB")
# print(part2)

# 3.데이터를 쪼개서 여러번 가져오기 => 한번씩 가져오고 처리하고 또 가져와야됨
# 청크 사이즈만큼만 불러오기

sales = part["sales_channel_id"].value_counts()*0

for chunk in pd.read_csv('./data/transactions_train.csv', chunksize=3000000): # 삼백만개씩
    print(chunk["sales_channel_id"].value_counts()) # 1, 2 값이 몇개씩 있는지
    sales = sales + chunk["sales_channel_id"].value_counts() # 짤라서 처리해서 더하기

print(sales)

#4. 데이터를 일부만 따로 저장
train2006 = train.loc[train['t_date'] > '2020-06-01']
train2006.to_csv("transactions_202006.py", index=False) # 데이터뽑기
