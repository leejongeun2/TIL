## 서버
---
1. ip와 도메인은 무엇일까요?
> https://developer.mozilla.org/ko/docs/Learn/Common_questions/How_does_the_Internet_work

* 네트워크에 연결 된 모든 컴퓨터에는 인터넷 프로토콜을 나타내는 고유한 주소인 ip주소를 가지고 있음
* ip 주소는 점으로 구분 된 네개의 숫자로 구성된다.
* 이러한 주소를 이용해 다른 컴퓨터를 찾을 수 있음
* ip 주소는 기억하기 어렵고 시간이 지나면서 변경 될 수 있기 때문에 ip 주소에 도매인 이름을 지정한다. 
* 웹 브라우저에 웹을 탐색 할 때 일반적을로 도메인 일므을 사용하여 웹 사이트에 접속할 수 있다. 

2. 클라이언트와 서버는 무엇일까요? 
> https://developer.mozilla.org/ko/docs/Learn/Getting_started_with_the_web/How_the_Web_works

> https://developer.mozilla.org/ko/docs/Learn/Common_questions/What_is_a_web_server

* 클라이언트: 웹 사용자의 인터넷이 연결 된 장치들과 이런 장치들에서 이용 가능한 웹에 접근하는 소프트웨어, 서비스를 요청하는 것
* 서버: 웹페이지, 사이트, 앱을 저장하는 컴퓨터

3. 정적 웹 사이트와 동적 웹 사이트의 차이점은 무엇일까요? Django는 무엇을 위한 도구인가요?
> https://developer.mozilla.org/ko/docs/Learn/Server-side/First_steps/Introduction
* 정적 웹사이트: 특별한 요청이 들어올 때, 서버에서 하드코딩된 동일한 콘텐츠를 반환, 서버에 미리 저장 된 html파일 그대로 내용이 변하지 않고 모든사용자에게 동일한 정보를 표시
* 동적 웹사이트: 필요할 때 동적으로 응답 콘텐츠가 생성, 보통 html템플릿에 있는 자리표시자에 데이터베이스에서 가져온 데이터를 넣어 생성됨
* 사용자 또는 지정된 환경을 기반으로 url에 대해 다른 데이터를 반환할 수 있으며, 응답을 반환하는 과정에서 다른 작업을 수행할 수 있음
* 장고: 파이썬으로 작성 된 오픈소스

4. HTTP는 무엇이고 요청과 응답 메시지 구성은 어떻게 되나요?
> https://developer.mozilla.org/ko/docs/Web/HTTP/Overview
* http는 웹에서 이루어지는 모든 데이터 교환의 기초, html문서와 같은 리소스들을 가져올 수 있도록 하는 클라이언트-서버 프로토콜
* 클라이언트에 의해 전송되는 메세지를 요청이라고 하며, 서버로부터 전송되는 메세지를 응답이라고 함, 요청은 하나의 객체이며 각각의 개별적인 요청들은 서버로 보내지고 서버는 요청을 처리하고 응답을 제공함

5. 프레임워크는 무엇일까요?(외부 자료 조사)
* 서비스 개발에 필요한 기능들을 미리 구현해서 모아 놓은 것


6. 웹 추천 영상

[https://www.youtube.com/watch?v=PUPDGbnpSjw]


