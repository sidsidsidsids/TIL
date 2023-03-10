# TIL

### 객체 지향 프로그래밍

> 컴퓨터 프로그램을 명령어의 목록으로 보는 시각에서 벗어나 여러 개의 독립된 단위
> 
> 프로그램을 여러 개의 독립된 객체들과 그 객체 간의 상호작용으로 파악하는 방법

- 절차 지향 프로그래밍
  
  - 전체 프로그램을 하나의 유기적인 흐름으로 연결
    
    - 기능 중심을 작성할 수 있다
    
    - 순서가 정해져 있어 실행이 빠르다
  
  - 하드웨어가 발전함에 따라 복잡한 설계가 요구됨
  
  - 따라서 생산성이 낮아 데이터가 중심인 객체 지향 도입

- 객체 지향 프로그래밍의 예시
  
  - 콘서트
    
    - 가수 객체
    
    - 감독 객체
    
    - 관객 객체

- 객체 지향의 장점
  
  - 계속해서 재사용이 가능
  
  - 그 자체로 데이터와 행동이 정의됨(독립적)
  
  - 객체 단위로 개발 가능하여 대규모 개발 가능
  
  - 개발 용이성, 유지 보수 편의성, 신뢰성을 바탕으로 생산성 증가

- 객체 지향의 단점
  
  - 설계 시 많은 노력과 시간이 필요함
  
  - 실행 속도가 상대적으로 느림

### OOP

- 객체(object) : **클래스에서 정의한 것을 토대로 메모리에 할당한 것**
                          변수, 자료 구조, 함수, 메서드가 될 수 있다.
  
  - 클래스를 만든다 == 타입을 만든다
  
  - 특징
    
    - 어떠한 타입(type)인가
    
    - 어떠한 속성(attribute)인가
    
    - 어떠한 조작법(method)을 가지는가

- 함수와의 차이 : 함수는 기능만 하고 끝나지만 객체는 데이터와 기능을 둘다 가짐

- 기본 문법
  
  - 클래스 정의
    
    - 나만의 타입
    
    - ` class Myclass: `
  
  - 인스턴스 생성
    
    - ` my_instance = Myclass() `
  
  - 메서드 호출
    
    - ` my_tnstance.my_method()`
  
  - 속성 접근
    
    - ` my_instance.my_attribute`

- 클래스와 인스턴스
  
  - 클래스 : 객체들의 분류/설계도
  
  - 인스턴스 : 하나하나의 실체/예

- 객체 비교하기
  
  - ==
    
    - 동등한 (equal)
    
    - 내용이 같으면 True
    
    - 실제로 동일한 대상을 가리키고 있다고 확인해 준 것은 아님
  
  - is
    
    - 동일한 (identical)
    
    - 동일한 객체를 가리키는 경우 True

- 속성
  
  - 클래스 변수 / 인스턴스 변수가 존재
  
  - 인스턴스에서 특정 속성에 접근하면 인스턴스-클래스 순으로 탐색

- 인스턴스 변수
  
  - 인스턴스가 개인적으로 가지고 있는 속성
  
  - 각 인스턴스들의 고유한 변수
  
  - 생성자 메서드에서 self.name 으로 정의
  
  - 인스턴스가 생성된 이후 instance.name 으로 접근 및 할당

- 클래스 변수

- self
  
  - 인스턴스 자기 자신
  
  - 파이썬에서 인스턴스 메서드는 호출 시 첫번째 인자로 인스턴스 자신이 전달됨

### OOP 메서드

> 메서드 : 특정 데이터 타입/클래스의 객체에 공통적으로 적용 가능한 행위(함수)

- 인스턴스 메서드
  
  - 인스턴수 변수를 사용하거나 인스턴스 변수에 값을 설정하는 메서드
  
  - 메서드의 기본
  
  - 매직 메서드
    
    - double underscore(____)가 있는 메서드
    
    - 특정 상황에서 자동으로 불림

- 클래스 메서드
  
  - 클래스 단위로 사용할 때
  
  - 호출 시 첫 인자로 클래스(cls)가 전달됨

- 정적 메서드
  
  - 인스턴스도, 클래스도 사용하지 않을 때


