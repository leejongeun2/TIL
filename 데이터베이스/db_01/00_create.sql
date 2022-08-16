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

-- csv import 하기
.mode csv 
.import health.csv healthcare
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