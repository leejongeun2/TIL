--8/19(금)실습==============================================

--1. 모든 테이블의 이름
--같은 테이블에 데이터베이스 접속(sqlite3 sample.sqlite3) 후 터미널에 .tables


--2. 모든 테이블의 데이터를 확인
--터미널에 .schema [테이블명] 입력

--3.앨범 테이블의 데이터를 출력
select * from albums order by Title limit 5

--4.고객 테이블의 행 개수 출력
select count(*) "고객 수" from customers
select * from customers

--5.고객 테이블에서 고객이 사는 나라가 usa인 고객의 first name, lastname을 출력
select FirstName "이름", LastName "성" from customers where country = "USA" order by FirstName desc limit 5


--6.송장(invoices) 테이블에서 `BillingPostalCode`가 `NULL` 이 아닌 행의 개수를 출력하세요.
select count(*) "송장수" from invoices where BillingPostalCode is not NULL
select * from invoices 

--7.송장(invoices) 테이블에서 `BillingState`가 `NULL` 인 데이터를 출력하세요.
select * from invoices where BillingState is NULL ORDER by InvoiceDate desc limit 5

--8.송장(invoices) 테이블에서 `InvoiceDate`의 년도가 `2013`인 행의 개수를 출력하세요.
select count(*), InvoiceDate from invoices where strftime('%Y', InvoiceDate) = '2013'
select InvoiceDate, strftime('%Y', InvoiceDate) from invoices

--9.고객(customers) 테이블에서 `FirstName`이 `L` 로 시작하는 고객의 `CustomerId`, `FirstName`, `LastName`을 출력하세요.
select CustomerId 고객id, FirstName 이름, LastName 성 from customers where FirstName like "L%" order by 고객id

--10.고객(customers) 테이블에서 각 나라의 고객 수와 해당 나라 이름을 출력하세요.
select count(*) 고객수, Country 나라 from customers group by Country order by 고객수 desc limit 5

--11.앨범(albums) 테이블에서 가장 많은 앨범이 있는 Artist의 `ArtistId`와 `앨범 수`를 출력하세요.
select ArtistId, count(*) as '앨범수' from albums group by ArtistId order by count(*) DESC limit 1
--재확인 필요
--서브쿼리 활용법
SELECT ArtistId, max("앨범 수") AS "앨범 수" FROM (SELECT ArtistId, count(*) AS "앨범 수" FROM albums GROUP BY ArtistId);



--12. 앨범(albums) 테이블에서 보유 앨범 수가 10개 이상인 Artist의 `ArtistId`와 `앨범 수` 출력하세요
select ArtistId, count(*) from albums group by ArtistId having count(*)>=10 order by count(*) desc

--13. 고객(customers) 테이블에서 `State`가 존재하는 고객들을 `Country` 와 `State`를 기준으로 그룹화해서 각 그룹의 `고객 수`, `Country`, `State` 를 출력하세요.
select count(*), Country, State from customers where state not null group by Country, State order by count(*) desc, country desc limit 5

--14. 고객(customers) 테이블에서 `Fax` 가 `NULL`인 고객은 'X' NULL이 아닌 고객은 'O'로 `Fax 유/무` 컬럼에 표시하여 출력하세요.
select fax, case when fax is null then 'x' when fax not null then 'o' end as "fax 유/무" from customers
select * from customers

--15. 점원(employees) 테이블에서 `올해년도 - BirthDate 년도 + 1` 를 계산해서 `나이` 컬럼에 표시하여 출력하세요.

select LastName, FirstName, (cast(strftime('%Y','now') as integer)-cast(strftime('%Y', BirthDate) as integer))+1 as '나이' from employees ORDER by EmployeeId
select ((strftime('%Y','now'))-(strftime('%Y', BirthDate)) as age from employees
select ((strftime('%Y','now')-strftime('%Y', BirthDate)) from employees

select cast(strftime('%Y','now') as integer) from employees

--16. 가수(artists) 테이블에서 앨범(albums)의 개수가 가장 많은 가수의 `Name`을 출력하세요.
select Name from artists where ArtistId = (select ArtistId from albums GROUP by ArtistId order by count(title) desc LIMIT 1)


select ArtistId from albums GROUP by ArtistId order by count(title) desc LIMIT 1 

--17. 장르(genres) 테이블에서 음악(tracks)의 개수가 가장 적은 장르의 `Name`을 출력하세요.


select name from genres where GenreId = (select GenreId from tracks group by GenreId order by count(*) limit 1)


select GenreId from tracks group by GenreId order by count(*) limit 1

select * from tracks
select * from genres


