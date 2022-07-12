#미세먼지 농도에 따른 등급일 떄, dust값에 따라 등급을 출력하는 조건식
dust = 100
# dust가 150보다 크면, 매우 나쁨
if dust > 150 :
    print('매우나쁨')
# 80보다 크면, 나쁨
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
#좋은
else:
    print('좋음')
    