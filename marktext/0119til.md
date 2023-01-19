# TIL

### 함수 응용

- map
  
  - `map(function,iterable)` : iterable에 function를 적용한다

- filter
  
  - `filter(function,iterable)` : iterable의 모든 요소에 function를 적용하고 결과가 True인 것들을 filter object로 반환

- zip
  
  - `zip(*iterables)` : 복수의 iterable을 모아 튜플을 원소로 하는 zip object 반환

- lambda
  
  - `lambda 매개변수 : 매개변수를 이용한 리턴값` : mab표현식을 계산한 결과값을 반환하는 함수

- 재귀함수
  
  - 자기 자신을 호출하는 함수 (ex : n! = n * (n-1)! ... )

### 함수 가변

- 패킹/언패킹 연산자 *
  
  - 패킹 : 대입문의 좌변 변수에 위치하며 우변의 객체 수가 좌변의 변수 수보다 많을 경우 객체를 순서대로 대입함
  
  - 언패킹 : argument 이름이 *로 시작하는 경우 argument unpacking이라 함
  
  - 몇개의 키워드 인자를 받을 지 모를 때 가변 키워드 인자 **kwargs 사용

### 모듈과 패키지

> 모듈 : python file(.py), 특정 기능을 모아 하나의 파일로 만든 것
> 
> 패키지 : 다양한 파일을 하나의 폴더로 만든 것
> 
> 라이브러리 : 다양한 패키지를 하나의 묶음으로 묶은 것

- pip install은 bash, cmd에서 사용되는 명령어
  
  - 명령어 : install, uninstall, list, show, freeze

- 폴더 안에 '_ _ init__.py' 파일이 있으면 파이썬은 폴더를 패키지로 인식

### 가상환경

> 특정 폴더에 가상 환경이 있고 이를 활성화시켜 사용한다
> 
> 
