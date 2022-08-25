--1번======================
SELECT * from playlist_track as A ORDER BY A.PlaylistId DESC LIMIT 5

select * from playlist_track

--2번======================

select * from tracks b order by b.TrackId limit 5
select count(*) from tracks
select * from tracks

--3번=========================

select PlaylistId, Name from playlist_track join tracks on playlist_track.TrackId = tracks.TrackId order by PlaylistId desc limit 10
select PlaylistId, Name from playlist_track left outer join tracks on playlist_track.TrackId = tracks.TrackId order by PlaylistId desc limit 10


--4번=========================`PlaylistId`가 `10`인 track 데이터를 함께 출력하세요. 단, PlaylistId, Name 컬럼을 `Name` 기준으로 내림차순으로 5개만 출력하세요.
select PlaylistId, Name from playlist_track join tracks on playlist_track.TrackId = tracks.TrackId where PlaylistId = 10 order by Name desc limit 5
select PlaylistId, Name from playlist_track join tracks on playlist_track.TrackId = tracks.TrackId

--5번=========================
select count(*) from tracks join artists on tracks.Composer = artists.Name
select * from artists

--6번=========================
select count(*) from tracks left outer join artists on tracks.Composer = artists.Name

--7번=====================
select a.Composer, b.Name from tracks a join artists b on a.Composer = b.Name
select a.Composer, b.Name from tracks a left outer join artists b on a.Composer = b.Name

select Composer, Name from tracks join artists on tracks.Composer = artists.Name
--테이블명 입력 안했을 때 name컬럼이 애매하다는 오류 뜸(어느테이블의 칼럼인지 명시 필요) > 확인 필요

select tracks.Composer, artists.Name from tracks join artists on tracks.Composer = artists.Name

--8번================================
select InvoiceLineId, InvoiceId from invoice_items ORDER by InvoiceId limit 5

--9번===============================
select InvoiceId, CustomerId from invoices ORDER by InvoiceId limit 5

--10번=============================
select InvoiceLineId, invoices.InvoiceId from invoice_items join invoices on invoice_items.InvoiceId = invoices.InvoiceId order by invoices.InvoiceId desc limit 5
select InvoiceLineId, invoices.InvoiceId from invoice_items join invoices on invoice_items.InvoiceId = invoices.InvoiceId order by invoice_items.InvoiceId desc limit 5
--11번==============================
select invoices.InvoiceId, customers.CustomerId from invoices join customers on invoices.CustomerId = customers.CustomerId order by invoices.InvoiceId desc limit 5
select * from invoices
select * from invoice_items
select * from customers
--답안
SELECT A.InvoiceId, B.CustomerId FROM invoices A
INNER JOIN customers B
ON A.CustomerId = B.CustomerId
ORDER BY A.InvoiceId DESC
LIMIT 5;

--12번==============================
-- 각 invoices_item(상품)을 포함하는 invoice(송장)와 해당 invoice를 받을 customer(고객) 데이터를 모두 함께 출력하세요.
-- 단, InvoiceLineId, InvoiceId, CustomerId 컬럼을 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.
select invoice_items.InvoiceLineId, invoices.InvoiceId, invoices.CustomerId from invoices join invoice_items on invoices.InvoiceId = invoice_items.InvoiceId join customers on invoices.CustomerId = customers.CustomerId ORDER by invoices.CustomerId desc limit 5
select invoice_items.InvoiceLineId, invoice_items.InvoiceId, customers.CustomerId from invoice_items join invoices on invoice_items.InvoiceId = invoices.InvoiceId join customers on invoices.CustomerId = customers.CustomerId ORDER by invoice_items.InvoiceId desc limit 5 
--이미 인보이스 아이템 테이블에 두 개 컬럼이 있어서 해당 테이블의 컬럼이 조인 된 테이블에 두개 있어서 두개 컬럼이 변경 됨

select invoice_items.InvoiceLineId, invoices.InvoiceId, invoices.CustomerId from invoices join invoice_items on invoices.InvoiceId = invoice_items.InvoiceId join customers on invoices.CustomerId = customers.CustomerId
select invoice_items.InvoiceLineId, invoice_items.InvoiceId, customers.CustomerId from invoice_items join invoices on invoice_items.InvoiceId = invoices.InvoiceId join customers on invoices.CustomerId = customers.CustomerId 

--답안
SELECT A.InvoiceLineId, A.InvoiceId, C.CustomerId 
FROM invoice_items A
    INNER JOIN invoices B
        ON A.InvoiceId = B.InvoiceId
    INNER JOIN customers C
        ON B.CustomerId = C.CustomerId
ORDER BY A.InvoiceId DESC
LIMIT 5;

--13번=============================
--각 cusotmer가 주문한 invoices_item의 개수를 출력하세요.
--| 단, CustomerId와 개수 컬럼을 `CustomerId` 기준으로 오름차순으로 5개만 출력하세요.

select customers.CustomerId, count(*) 
from customers 
join invoices 
on customers.CustomerId = invoices.CustomerId 
join invoice_items 
on invoice_items.InvoiceId = invoices.InvoiceId 
GROUP BY customers.CustomerId
ORDER BY customers.CustomerId ASC limit 5
LIMIT 5; 

select customers.CustomerId, count(*) 
from customers join invoices 
on customers.CustomerId = invoices.CustomerId join invoice_items 
on invoice_items.InvoiceId = invoices.InvoiceId
-- CustomerId	count(*)
-- 1	412
--
--


SELECT * FROM invoices A
    INNER JOIN customers B 
    ON A.CustomerId = B.CustomerId
--1. 고객id로 조인한 서브쿼리 넣기 

sELECT C.CustomerId, count(*) FROM invoice_items A
INNER JOIN (
    SELECT * FROM invoices A
    INNER JOIN customers B
    ON A.CustomerId = B.CustomerId
) C
ON A.InvoiceId = C.InvoiceId
--GROUP BY C.CustomerId
ORDER BY C.CustomerId ASC
LIMIT 5;

--답안
SELECT C.CustomerId, count(*) FROM invoice_items A
INNER JOIN (
    SELECT * FROM invoices A
    INNER JOIN customers B
    ON A.CustomerId = B.CustomerId
) C
ON A.InvoiceId = C.InvoiceId
GROUP BY C.CustomerId
ORDER BY C.CustomerId ASC
LIMIT 5;