###  1. 흡연 여부(smoking)로 구분한 각 그룹의 컬렴명과 그룹의 사람의 수를 출력하시오.

```sql 
select count(*), smoking from healthcare group by smoking
```

###  2. 음주 여부(is_drinking)로 구분한 각 그룹의 컬렴명과 그룹의 사람의 수를 출력하시오.

```sql 
select count(*), is_drinking from healthcare group by is_drinking

--
count(*)	is_drinking	blood_pressure
415119	0	127
584685	1	114
196		131
```

### 3. 음주 여부로 구분한 각 그룹에서 혈압(blood_pressure)이 200이상인 사람의 수를 출력하시오.

```sql
select count(*), is_drinking from healthcare group by is_drinking having blood_pressure>=120

count(*)	is_drinking	blood_pressure
415119	0	127
196		131
--위 2번까지 진행후, 거기서 120이상으로 필터링




--이게 더 정확: 집계 발생 전 먼저 필터링하고 그 것을 집계한 것이기 때문 
select count(*), is_drinking, blood_pressure from healthcare where blood_pressure>=200 and blood_pressure <> '' group by is_drinking
count(*)	is_drinking	blood_pressure
268500	0	127
370557	1	130
135		131
---집계 발생 전, 120이상인 경우 갯수세기, 갯수 센 후 그 갯수를 카운트하기

select count(*) from healthcare where blood_pressure>=120 and is_drinking = 0
count(*)
268500
```

### 4. 시도(sido)에 사는 사람의 수가 50000명 이상인 시도의 코드와 그 시도에 사는 사람의 수를 출력하시오.

```sql
select count(*), sido from healthcare group by sido having count(*)>50000
```

### 5. 키(height)를 기준으로 구분하고, 각 키와 사람의 수를 출력하시오.

> 단, 사람의 수를 기준으로 내림차순으로 5개까지 출력하시오.

```sql
select height, count(*) from healthcare GROUP by height
```

### 6. 키(height)와 몸무게(weight)를 기준으로 구분하고, 몸무게와, 키, 해당 그룹의 사람의 수를 출력하시오. 

> 단, 사람의 수를 기준으로 내림차순 5개까지 출력하시오.

```sql
select height, weight, count(*) from healthcare group by height, weight
```

### 7. 음주여부에 따라 평균 허리둘레(waist)와 사람의 수를 출력하시오.

```sql 
select count(*), avg(waist) from healthcare group by is_drinking
```

### 8. 각 성별(gender)의 평균 왼쪽 시력(va_left)과 평균 오른쪽 시력(va_right)를 출력하시오.

> 단, 평균 왼쪽 시력과 평균 오른쪽 시력의 컬럼명을 '평균 왼쪽 시력' '평균 오른쪽 시력'로 표시하고, 평균 시력은 소수점 둘째 자리까지 출력하시오.

```sql
select round(avg(va_left),2) '평균 왼쪽 시력' , round(avg(va_right),2) '평균 오른쪽 시력', gender from healthcare group by gender
```

### 9. 각 나이대(age)의 평균 키와 평균 몸무게를 출력하시오.

> 단, 평균 키와 평균 몸무게의 컬럼명을 '평균 키' '평균 몸무게'로 표시하고, 평균키가 160 이상 평균 몸무게가 60 이상인 데이터만 출력하시오.

```sql
select avg(height) '평균 키', avg(weight) '평균 몸무게' from healthcare group by age having avg(height)>=160 and avg(weight)>=60
```

### 10. 음주 여부(is_drinking)와 흡연 여부(smoking)에 따른 평균 BMI를 출력하시오.

> 단, 음주 여부 또는 흡연 여부가 공백이 아닌 행만 사용하세요.

```sql
select avg(weight/((height*height)*0.0001)) from healthcare where is drinkig != '' and smoking != '' group by is_drinking, smoking
```