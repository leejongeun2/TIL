##   flexbox froggy

* 컨테이너: 플렉스? 
* 요소: 개구리

---

### Justify-content

> 이 속성은 다음 값들을 인자로 받아 요소들을 가로선 상에 정렬

* `flex-start`: 요소들을 컨테이너의 왼쪽으로 정렬합니다.
* `flex-end`: 요소들을 컨테이너의 오른쪽으로 정렬합니다.
  * **[flex-direction](#flex-direction)의 Column-reverse 또는 row-reverse를 사용하면 요소들의 start end 순서가 바뀜**
  * **[flex-direction](#flex-direction)의 방향이 컬럼일 경우, justify-content가 세로로, align-items 방향이 가로로 바뀜**
* `center`: 요소들을 컨테이너의 가운데로 [정렬](#속성)합니다.
* `space-between`: 요소들 사이에 동일한 간격을 두고, 양끝에 간격 없음
* `space-around`: 요소들 주위에 동일한 간격을 두고,간 박스를 둘러싼 영역(간격 안에서)에서 적용
* `space-evenly`: 요소들 주위에 동일한 간격을 두고, 전체 영역에서 동일한 공백이 적용

### align-items

> 이 속성은 다음의 값들을 인자로 받아 요소들을 세로선상에서 정렬

- `flex-start`: 요소들을 컨테이너의 꼭대기로 정렬합니다.
- `flex-end`: 요소들을 컨테이너의 바닥으로 정렬합니다.
- `center`: 요소들을 컨테이너의 세로선 상의 가운데로 정렬합니다.
- `baseline`: 요소들을 컨테이너의 시작 위치에 정렬합니다.
- `stretch`: 요소들을 컨테이너에 맞도록 늘립니다.

### flex-direction

> 이 속성은 다음의 값들을 인자로 받아 컨테이너 안에서 요소들이 정렬해야 할 방향을 지정합니다. 

- `row`: 요소들을 텍스트의 방향과 동일하게 정렬합니다.
- `row-reverse`: 요소들을 텍스트의 반대 방향으로 정렬합니다.
- `column`: 요소들을 위에서 아래로 정렬합니다.
- `column-reverse`: 요소들을 아래에서 위로 정렬합니다.

### order

> row나 column의 순서를 역으로 바꾸는 것만으로는 충분하지 않을때, order속성을 각 요소에 적용할 수 있음
>
> 기본 값은 0이며,주어진 숫자에 따라 우선순위가 결정 됨, 양수나 음수로 바꿀 수 있음
>
> 배치순서
>
> 숫자가 자리가 아니라, 우선순위임

* Order = 1 

### align-self

> 개별 요소에 적용할 수 있는 또 다른 속성
>
> [align-items](#align-items)가 사용하는 값들을 인자로 받으며, 그 값들은 지정한 요소에만 적용
>
> 개별 아이템을 크로스축 기준으로 정렬

* Flex-start
* Flex-end
* center
* strethch
* Baseline

### flex-wrap

* `nowrap`: 모든 요소들을 한 줄에 정렬합니다.
* `wrap`: 요소들을 여러 줄에 걸쳐 정렬합니다.
* `wrap-reverse`: 요소들을 여러 줄에 걸쳐 반대로 정렬합니다.

### flex-flow

* `flex-direction`과 `flex-wrap`이 자주 같이 사용되기 때문에, `flex-flow`가 이를 대신할 수 있습니다. 

  공백문자를 이용하여 두 속성 값들을 인자로 받음

* Column wrap: 세로선 상의 여러줄에 걸쳐 정렬하기 위해

* Row  wrap: 가로선 상의 여러줄에 걸쳐 정렬하기 위해

### align-content

> 크로스축을 기준으로 공간 배분(아이템이 한 줄로 배치되는 경우 확인할 수 없음!)

- `flex-start`: 여러 줄들을 컨테이너의 꼭대기에 정렬합니다.
- `flex-end`: 여러 줄들을 컨테이너의 바닥에 정렬합니다.
- `center`: 여러 줄들을 세로선 상의 가운데에 정렬합니다.
- `space-between`: 여러 줄들 사이에 동일한 간격을 둡니다.
- `space-around`: 여러 줄들 주위에 동일한 간격을 둡니다.
- `stretch`: 여러 줄들을 컨테이너에 맞도록 늘립니다.



## learn css

---

### 박스모델



