import requests, bs4 # HTML source를 tag별 계층 구조를 파악하기 쉽게 parse tree 형태로 변환해주는 라이브러리 입니다.

page_no = 2
page_url = f"https://finance.naver.com/sise/sise_index_day.naver?code=KPI200&page={page_no}"
# print(page_url) #https://finance.naver.com/sise/sise_index_day.naver?code=KPI200&page=1

source = requests.get(page_url).text # ~을 주세요. (url, params=none, **kwargs)

# print(source) # <Response [200]> => 정상적으로 받아왔다. , text 붙이면 태그안에 문자를 가져올 수 있음

source1 = bs4.BeautifulSoup(source) #BeautifulSoup : html 정리(함수를 사용해서 불러온 html source를 "lxml" parser로 parsing 합니다.)

# print(source1.prettify()) #함수는 HTML source를 tab을 기준으로 "이쁘게" 보여줍니다.

prices = source1.find_all('td', class_='number_1') # HTML source에서 조건을 만족하는 모든 tag을 가져오는 함수입니다.
# 같은 클래스가 여러개 있을 때, 뽑아내는방법!!!! => 4개씩 점프하면서 !가져오기 => 슬라이싱 사용
price_list = []
for price in prices[::4]:
    price_list.append(price.text)
    
# print(price_list) # ['323.69', '324.90', '325.63', '320.55', '318.83', '325.86']

dates = source1.find_all("td", class_="date") # 날짜만 가져오기
# print(dates) => [<td class="date">2023.02.10</td>, <td class="date">2023.02.09</td>, <td class="date">2023.02.08</td>, <td class="date">2023.02.07</td>, <td class="date">2023.02.06</td>, <td class="date">2023.02.03</td>]
date_list = []
for date in dates:
    date_list.append(date.text)

# print(date_list) # ['2023.02.10', '2023.02.09', '2023.02.08', '2023.02.07', '2023.02.06', '2023.02.03'] 날짜정보만 추출하여 리스트로 만듦

# 꿀팁: html에 어딨는지 알려주는 것(마우스 오른쪽 -> capy -> xpath) /html/body/div/table[1]/tbody/tr[3]/td[1]
# 꿀팁: a태그 뽑을 때 바로 위에 것 뽑기

last_url = source1.find_all("td", class_="pgRR")[0].find_all("a")[0]["href"]
last_page = last_url.split('&page=')[-1]
print(last_page)