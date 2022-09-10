### csv 파일 db에 넣는 방법!

 ✔️ sqlite3 tutorial.sqlite3 내 디비를 이렇게 디비를 열어야함(아래 1번)

✔️ 헬스케어 csv파일은 데이터를 그대로 디비에 넣어둔 것, 디비에 반영 시킨 것

✔️ csv 파일 넣기 !! 

1. 디비 접속 
2.  테이블을 만들고(크리에이티드 테이블) 
3. 모드 csv ( 반드시 같은 디렉토리에 있는 csv 파일을 <만든 테이블이름>으로 넣기 !! 
- import health.csv 만든 테이블명
    - 같은 디렉토리에 있는 health.csv파일을 만든 테이블명으로

1. 데이터베이스 생성하기 > sqlite라는 파일 생김(데이터 베이스 생김), 파일 형태로 관리됨
    1. sqlite3 tutorial.sqlite3 > 이미 생성 된 후라면 접속할 때도 해당 문구 쓰임
    2. .database
2. csv파일을 위 디비에 테이블로 만들기 - 컴마로 구분 된 값 가져오기
    1. .mode csv
    2. import hellodb.csv 테이블명 > csv파일을 특정 테이블로 가져오기