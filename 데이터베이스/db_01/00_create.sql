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


--8/17
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
select count(*) from healthcare where (weight/((height*height)*0.0001)>=30);

--12번
select id, weight/((height*height)*0.0001) AS bmi FROM healthcare where smoking = 3 order by weight/((height*height)*0.0001) desc limit 5

--12번 연습
SELECT weight, (height  * height) * 0.0001 , weight / ((height * height) * 0.0001), weight / ((height*0.01)*(height*0.01))FROM healthcare 
        
SELECT ((height * height) * 0.0001) FROM healthcare
SELECT weight, (height  / 100) , (height * 0.01)  FROM healthcare        