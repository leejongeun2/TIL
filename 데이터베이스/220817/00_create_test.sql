-- 테이블 만들기
CREATE TABLE healthcare (
id PRIMARY KEY,
sido INTEGER NOT NULL,
gender INTEGER NOT NULL,
age INTEGER NOT NULL,
height INTEGER NOT NULL,
weight INTEGER NOT NULL,
waist REAL NOT NULL,
va_left REAL NOT NULL,
va_right REAL NOT NULL,
blood_pressure INTEGER NOT NULL,
smoking INTEGER NOT NULL,
is_drinking BOOLEAN NOT NULL
);

--8/16(화)
-- csv import 하기
.mode csv 
.import health.csv healthcare

SELECT * FROM healthcare
--1번
SELECT COUNT(*) FROM healthcare;

--2번
select * from healthcare where age < 10;
--3번
select * from healthcare where gender = 1;
--4번
select count(*) from healthcare where smoking = 3 and is_drinking =1;

--5번
select count(*) from healthcare where va_left >= 2.0 and va_right >= 2.0;
--6번
select * from healthcare where va_left >= 2.0 and va_right >= 2.0;
--7번
select distinct sido from healthcare;


--8/17===============================================
--1번
SELECT COUNT(*) FROM healthcare;

--2번
select min(age), max(age) from healthcare;

--3번
select min(height), max(weight) from healthcare;

--4번
select height from healthcare where height >= 160 and height<=170;

--5번
select * from healthcare where is_drinking = 1 and waist <> "" order by waist desc limit 5;
select * from healthcare where is_drinking = 1 and waist != '' order by waist desc limit 5;
--6번

select count(*) from healthcare where va_left >= 1.5 and va_right >= 1.5 and is_drinking = 1

--7번

select count(*) from healthcare where blood_pressure < 120

--8번

select avg(waist) from healthcare where blood_pressure >= 140

--9번

select avg(height), avg(weight) from healthcare where gender =1

--10번 
select id, height, weight from healthcare where height=195 order by weight desc limit 1 offset 1

select id, height, weight from healthcare order by height desc, weight desc limit 1 offset 1

select id, height, weight from healthcare order by height desc, weight desc





--11번
select count(*) from healthcare where weight/((height*0.01)*(height*0.01))>=30;

--12번
select id, weight/((height*height)*0.0001) AS bmi FROM healthcare where smoking = 3 order by bmi desc limit 5

--12번 연습
SELECT weight, (height  * height) * 0.0001 , weight / ((height * height) * 0.0001), weight / ((height*0.01)*(height*0.01))FROM healthcare 
        
SELECT ((height * height) * 0.0001) FROM healthcare
SELECT weight, (height  / 100) , (height * 0.01)  FROM healthcare





--8/18(목)===============================================================
--replace
SELECT first_name, phone, replace(phone, '-', '') FROM users LIMIT 5;

--gruop by
--users에서 각 성씨가 몇명 씩 있는 조회? 
select count(*), last_name from users group by last_name;

--평균보다 많은 사람? 
--group by where쓰고 싶을 때

select last_name, count(last_name) from users WHERE count

--1번-------------------
select * from healthcare

select count(*), smoking from healthcare group by smoking 

--2번---------------------
select count(*), is_drinking, blood_pressure from healthcare group by is_drinking
--각 그룹의 맨 앞 혈압이 나옴




--3번-------------
select count(*), is_drinking, blood_pressure from healthcare group by is_drinking having blood_pressure>=200
--아무 결과 안나옴, having 은 집계가 발생한 후 필터링, havig은 집계함수로 조건 줄 때

select count(*), is_drinking, blood_pressure from healthcare where blood_pressure>=200 and blood_pressure<>'' group by is_drinking
-- where은 집계 발생 전 필터링
-- 공백제거

select count(*), is_drinking, blood_pressure from healthcare where blood_pressure>=200 group by is_drinking
-- 공백 제거 안한 거 

select * from healthcare where blood_pressure>=200 and blood_pressure<>'' group by is_drinking
select * from healthcare where blood_pressure>=200 group by is_drinking


select count(*), is_drinking, blood_pressure from healthcare GROUP by is_drinking




select blood_pressure, is_drinking from healthcare where blood_pressure>=200 and blood_pressure<>'' group by is_drinking
select blood_pressure, is_drinking from healthcare where blood_pressure>=200 group by is_drinking
--각 그룹의 맨 앞 혈압이 나옴


select blood_pressure from healthcare where blood_pressure>=200 and is_drinking = 0
--확인해보니 맨 위에 공백 있음
select blood_pressure from healthcare where blood_pressure>=200 and blood_pressure<>'' and is_drinking = 0
-- 확인해보니 맨 위에 228, 220있음







--4번-----------------
select count(*), sido from healthcare group by sido having count(*)>50000

--5번-------------------
select height, count(*) from healthcare GROUP by height 

--6번-------------------
select height, weight, count(*) from healthcare group by height, weight order by count(*) desc limit 5

--7번---------------------
select count(*), avg(waist), is_drinking from healthcare group by is_drinking 

--8번---------------------
select round(avg(va_left),2) '평균 왼쪽 시력' , round(avg(va_right),2) '평균 오른쪽 시력', gender from healthcare group by gender

--9번-----------------------
select avg(height) '평균 키', avg(weight) '평균 몸무게' from healthcare group by age having avg(height)>=160 and avg(weight)>=60

--10번-----------------------
select is_drinking, smoking, avg(weight/((height*height)*0.0001)) from healthcare group by is_drinking, smoking



--8/19(금)=======================================
--특정 성씨별 가장 적은 나이
select last_name, min(age) from users group by last_name

--서브쿼리 다중행컬럼--
--특정 성씨별로 가장 적은 나이 모두--
select last_name, first_name, age from users where(last_name, age) in 
(select last_name, min(age) from users group by last_name) order by last_name;



