# TIL

### 함수

> Decomposition(분해)와 Abstraction(추상화)
> 
> 특정한 기능을 하는 코드의 조각(묶음)

### 함수 기초

- 내장 함수
  
  - 파이썬에 기본적으로 포함된 함수

- 외장 함수
  
  - import 문을 통해 사용하는 외부 라이브러리에서 제공하는 함수

- 사용자 정의 함수
  
  - 직접 사용자가 만드는 함수

- 기본 구조
  
  - 선언과 호출(Define & Call)
  
  - 입력(Input)
  
  - 문서화(Docstring)
  
  - 범위(Scope)
  
  - 결과값(Output) : return 값이 없는 경우 None을 반환함

### 함수의 입력

- Parameter : 함수를 정의할 때 함수 내부에서 사용되는 변수

- Argument : 함수를 호출할 때 넣어주는 값
  
  - Positional Arguments : 기본적으로 호출 시 위치에 따라 함수 내에 전달
  
  - Keyword Arguments : 직접 변수의 이름으로 특정 Argument 전달함
  
  - Default Arguments Values : 기본값을 지정하여 따로 값을 설정하지 않도록 함 

### 파이썬의 범위(scope)

> 함수는 코드 내부에 local scope를 생성하며 그 외 공간은 global scope로 구분

- Namespace : 식별자들을 기억하는 공간
  
  - Built-in(정의하지 않고 사용할 수 있음) (ex : print)
  
  - Global
  
  - Enclosing
  
  - Local (지역 범위 중 가장 작음) (크기 순서로 Local이 제일 작음)

- scope : 변수의 제한 범위, 찾는 순서는 Local -> Enclosed -> Global -> Built-in
  
  - global scope
  
  - local scope
  
  ` def 함수1 :
       x = 5        # Enclosed
       def 함수2 :
           x = 6    # Local
           return
       print(x)
   print(x)         # Global`
  
  - **함수 내 필요한 상위 scope 변수는 argument로 넘겨서 활용**

- variable
  
  - global variable
    
    - global에 나열되면 같은 코드 블록에서 global 앞에 등장할 수 없다
    
    - global에 나열되면 parameter, for 루프 대상, 클래스/함수 등으로 정의 X
  
  - local variable
  
  - nonlocal
    
    - global을 제외한 가장 가까운 scope의 변수를 연결
      
      - nonlocal에 나열되면 같은 코드 블록에서 ~
      
      - parameter, for 루프 대상, 클래스/함수 등으로 ~
  
  - **함수로 값을 바꾸고자 한다면 항상 argument로 넘기고 리턴 값을 사용하기**

- 변수 수명주기(lifecycle)
  
  - built-in scope
    
    - 파이썬이 실행된 이후부터 영원히 유지
  
  - global scope
    
    - 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지
  
  - local scope
    
    - 함수가 호출될 때 생성되고, 종료될 때까지 유지












