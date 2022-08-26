-- 이름을 사전 순으로 정렬하면 다음과 같으며, 'Jewel', 'Raven', 'Sugar'
--'Raven'이라는 이름을 가진 개와 고양이가 있으므로, 이 중에서는 보호를 나중에 시작한 개를 먼저 조회합니다.
SELECT ANIMAL_ID, NAME, DATETIME FROM ANIMAL_INS ORDER BY NAME, DATETIME DESC

--동물 보호소에 가장 먼저 들어온 동물의 이름을 조회 => LIMIT 역할은 몇개 조회할 것인지, offset 역할은 어디서 조회할 것인지(limit2 offset1 인 경우, limit몇개 조회, 2번쨰부터
SELECT NAME FROM ANIMAL_INS ORDER BY DATETIME LIMIT 1

--동물 보호소에 가장 먼저 들어온 동물은 언제 들어왔는지 조회
SELECT datetime from ANIMAL_INS order by datetime limit 1;
SELECT * FROM (SELECT DATETIME FROM ANIMAL_INS ORDER BY DATETIME) WHERE ROWNUM <= 1;
SELECT min(datetime) from animal_ins;

--동물 이름이 null이 아니고, 중복값 제거하여 총 들어온 이름 수 조회
SELECT COUNT(DISTINCT NAME) AS NAME_COUNT FROM ANIMAL_INS WHERE NAME IS NOT NULL 

--동물 보호소에 들어온 동물 중 고양이와 개가 각각 몇 마리인지 조회하는 SQL문을 작성해주세요. 이때 고양이를 개보다 먼저 조회해주세요.
SELECT ANIMAL_TYPE, COUNT(*) FROM ANIMAL_INS GROUP BY ANIMAL_TYPE ORDER BY ANIMAL_TYPE

--동물 보호소에 들어온 동물 이름 중 두 번 이상 쓰인 이름과 해당 이름이 쓰인 횟수를 조회하는 SQL문을 작성해주세요. 이때 결과는 이름이 없는 동물은 집계에서 제외하며, 결과는 이름 순으로 조회해주세요.
SELECT NAME, COUNT(NAME) FROM ANIMAL_INS WHERE NAME <> "" GROUP BY NAME HAVING COUNT(NAME) >= 2 ORDER BY NAME

--보호소에서는 몇 시에 입양이 가장 활발하게 일어나는지 알아보려 합니다. 09:00부터 19:59까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문을 작성해주세요.
SELECT hour(DATETIME) as hello, count(DATETIME) --시간대로 추출하려면 hour 함수 사용
from ANIMAL_OUTS
where hour(DATETIME) between 9 and 19
group by hello
order by hello 

--동물 보호소에 들어온 동물 중, 이름이 없는 채로 들어온 동물의 ID를 조회하는 SQL 문을 작성해주세요. 단, ID는 오름차순 정렬
SELECT ANIMAL_ID FROM ANIMAL_INS WHERE NAME IS NULL ORDER BY ANIMAL_ID

--동물 보호소에 들어온 동물 중, 이름이 있는 동물의 ID를 조회하는 SQL 문을 작성해주세요. 단, ID는 오름차순 정렬되어야 합니다.
SELECT ANIMAL_ID FROM ANIMAL_INS WHERE NAME IS NOT NULL ORDER BY ANIMAL_ID

--동물의 생물 종, 이름, 성별 및 중성화 여부를 아이디 순으로 조회하는 SQL문을 작성해주세요. 이때 프로그래밍을 모르는 사람들은 NULL이라는 기호를 모르기 때문에, 이름이 없는 동물의 이름은 "No name"으로 표시해 주세요.

SELECT 
    INS.ANIMAL_TYPE,
    CASE 
        WHEN INS.NAME IS NULL THEN "No name"
        ELSE NAME        
    END AS NAME,
    INS.SEX_UPON_INTAKE
FROM ANIMAL_INS INS

--천재지변으로 인해 일부 데이터가 유실되었습니다. 입양을 간 기록은 있는데, 보호소에 들어온 기록이 없는 동물의 ID와 이름을 ID 순으로 조회하는 SQL문을 작성해주세요.
--out에는 있는데, in에는 없는 것 => out기준으로 left join 단, 보호소에 들어온 기록이 없는 동물을 추출해야 되기 때문에 in테이블의 null값을 추출 
-- out테이블에서
SELECT
    ao.ANIMAL_ID,
    ao.NAME
from ANIMAL_OUTS ao
    left join ANIMAL_INS ai
        on ai.ANIMAL_ID = ao.ANIMAL_ID --동일한 키로 찾음
where ai.ANIMAL_ID is null --is null이 있는 경우, 
order by ao.ANIMAL_ID;

--관리자의 실수로 일부 동물의 입양일이 잘못 입력되었습니다. 보호 시작일보다 입양일이 더 빠른 동물의 아이디와 이름을 조회하는 SQL문을 작성해주세요. 이때 결과는 보호 시작일이 빠른 순으로 조회해야합니다.
--out에서 잘못 입력 됨
SELECT I.ANIMAL_ID, I.NAME
FROM ANIMAL_INS AS I
JOIN ANIMAL_OUTS AS O --이너조인
ON I.ANIMAL_ID = O.ANIMAL_ID --키로 묶어줌
WHERE I.DATETIME > O.DATETIME --보호시작일 > 입양일이 더 작음(더 옛날) => 입양일이 더 커야 됨(더 나중이니까) 
ORDER BY I.DATETIME ASC --보호 시작일 내림차순
