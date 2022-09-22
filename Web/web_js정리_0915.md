## 01_js.html

---

### alert

* ```javascript
  <script>
    console.log("")
    alert('')
  </script>
  // 알럿 창 노출(창 안에 문구는 alert 안 텍스트)
  
  console.log('hello, js!')
  //개발자 도구 검사 
  //개발자도구 > 검사 > 콘솔 : 로그가 찍혀있음
  //콘솔.log(--) 괄호 안에 넣어야 저장 후 개발자도구에서 볼 수 있음
  
  * 자바스크립트 코드를 작성해볼 수 있는 곳
  * 콘솔.log에 작성하면 콘솔창에서 실행 될 것임
  * 콘솔 창을 앞으로 계속 열어서 실제 코드 작성, 자바스크립트 코드를 실행 결과를 디버깅하기 위해 출력 된 결과를 보는 곳
  ```

###  console.log()란? 위의 내용 추가설명

> 자바스크립트의 기본 동작과정은 
>
> 브라우저에게 `누구`는 `oo`를 `xx`해라! 형식으로 동작함
>
> 콘솔이 누구이며 주체가 될 것이고, 로그가 xx이며, ()안의 것이 00이다.
>
> 콘솔 => 객체
>
> 로그 => 메서드
>
> () => 매개변수

* 객체 안에 있는 메서드를 실행시켜 매개변수를 작동시키는 작업
* 결과를 콘솔창에 출력

### window

* Window.print() 

  * 프린트 창이 노출 됨

* window.confirm('messege')

  * 메세지와 함께 확인창이 노출 됨

  

### createelenment, innertext, queryselector, appendchild

### h1태그를 바디에 작성 없이 스크립트로만 구현 가능

* ```javascript
  
  const title = document.createelenment('h1')
  // h1요소를 만들고 => title => title은 요소 그 자체 => typeof(title)으로 타입 찍어보면 object로 나옴
  // 
  title.innertext = 'js기초'
  //타이틀에 텍스트 추가, 기존 있었던 텍스트 변경
  //속성을 바꾼거지, 개체가 바뀐 건 아님
  
  
  const body = document.queryselector('body')
  // 선택자로 body 태그를 가져와서
  // const 는 변수 선언 시 키워드 => 반복문에서는 let을 많이씀
  body.appendChild(title)
  //바디 태그에 자식 요소로 추가
  ```



## 02_select

---

### 요소 선택

* 선택해서 어딘가에 조작할 것임
* **선택자!!!가 가장 중요함**
  * 하나를 선택한다 => 쿼리셀렉터
  * 모든 결과를 선택한다. => 쿼리셀렉터올

```javascript
document.queryselector('#title') // 특정 태그, 특정 클래스, 특정 아이디를 괄호 안에 넣으면 해당하는 코드가 나옴
>> <h1 id="title">js기초</h1>

//selector과 selectorall의 차이
//selector은 한개만 반환, selectorall은 전체 반환
//리턴이 무엇인지 아는 것이 중요함

title.innerHTML = '<h2>우왕</h2>' => 바꿀 수 있음, 보안사유로 쓰지 않음
body.removeChild(a) => 삭제, 노드 아래에 있는 노드를 지우는 것
title.remove() => 이 노드 자체를 지우는것


```





## 03_attribyte

---

```javascript
a.setAttribute('href', 'https;//syllaverse.com') // href를 해당 주소로 넣어줌
a.getAttribute('href') // href의 주소값을 가져와!
//주소값 반환

h1.getAttribute('class') // 해당하는 클래스 가져옴
h1.setAttribute('class', 'blue') // 클래스를 블루로 바꿔줌

h1.classList //클래스를 모두 보여줌
h1.classList.replace('red', 'blue') // 클래스를 레드에서 블루로 바꿔주세요.
//리플레이스보다 토글을 더 많이씀

```



## 04_event

---



```javascript
<body>
    <h1>이벤트</h1>
    <button id="btn1">클릭</button>
    <script>
        const btn1 = document.querySelector('#btn1')
        btn1.addEventListener('click', function() {
            alert('버튼 클릭!!!!')
        })
    </script> 
</body>
// 버튼 클릭 시, 알럿이 뜸(텍스트는 '버튼클릭!!'' )



//---
<body>
    <h1>이벤트</h1>
    <button id="btn1">클릭</button>
    <script>
        const btn1 = document.querySelector('#btn1')
        //btn1이 클릭되면 함수실행
        btn1.addEventListener('click', function() {
            //h1 태그를 잡아서
            const h1 = document.querySelector('h1')
            // 클래스 블루를 토글하자
            h1.classList.toggle('blue')
        })
    </script>
    
</body>

//





//아래 코드 타이핑 치는 것을 받아서 그대로 이벤트 값으로 활용할 수 있음
<body>
    <h1>이벤트</h1>
    <button id="btn1">클릭</button>
    <input type="text">


    <script>
        const btn1 = document.querySelector('#btn1')
        //btn1이 클릭되면 함수실행
        btn1.addEventListener('click', function() {
            //h1 태그를 잡아서
            const h1 = document.querySelector('h1')
            // 클래스 블루를 토글하자
            h1.classList.toggle('blue')
        })

        //input
        const input = document.querySelector('input')
        input.addEventListener('input', function(e) {
            console.log(e.target.value)
        })
    </script>
    
</body>
</html>
```

