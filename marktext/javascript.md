### Event

> 네트워크 활동이나 사용자와의 상호작용 같은 사건의 발생을 알리기 위한 객체
> 
> 마우스 클릭, 키보드 인풋과 같은 사용자 행동으로 발생할 수도, 특정 메서드 호출하여 프로그래밍 적으로도 만들 수 있음

- Event 전파
  
  - DOM 요소에서 발생한 이벤트가 상위 노드에서 하위 노드 혹은, 그 반대로 전파되는 현상을 의미함
  
  - addEventListener 메서드를 사용하여 제어 가능

### 동기와 비동기

- 동기
  
  - 모든 일을 순서대로 하나씩 처리하는 것

- 비동기
  
  - 작업을 시작한 후 결과를 기다리지 않고 다음 작업을 처리하는 것 (병렬적)
  
  - JavaScript는 Single Thread 언어 (Thread : 작업을 처리할 때 이를 수행하는 주체)
  
  - 브라우저 환경에서의 비동기 동작 요소 (JavaScript Runtime)
    
    - JavaScript Engine : Call Stack
      
      - 요청이 들어올 때 마다 순차적으로 처리한는 Stack(LIFO)
      
      - 기본적으로 JavaScript의 Single Thread 작업 처리
    
    - Web API
      
      - 브라우저에서 제공하는 runtime 환경
      
      - 시간이 소요되는 작업을 처리 (setTimeout, DOM event, AJAX 요청 등)
    
    - Task Queue
      
      - 비동기 처리된 Callback 함수가 대기하는 Queue(FIFO)
    
    - Event Loop
      
      - Call Stack과 Task Queue를 지속적 모니터링
      
      - Stack이 비어 있는지 확인 후 비어 있다면 Queue에서 대기하는 오래된 작업을 Stack으로 Push
  
  - 비동기 처리 동작 방식 (브라우저 환경에서의 JavaScript의 비동기)
    
    - 모든 작업이 Call Stack으로 들어간 후 처리된다
    
    - 오래 걸리는 작업이 Call Stack으로 들어오면 Web API로 보내 별도 처리한다
    
    - Web API에서 처리가 끝난 작업들은 Task Queue에 순서대로 들어간다
    
    - Event Loop가 Call Stack이 비어 있는 것을 계속 체크하고 빈다면 Task Queue에서 가장 오래된 작업(가장 앞에 있는)을 Call Stack으로 보낸다

### Axios

> JavaScript의 HTTP 웹 통신을 위한 라이브러리

### Callback Function

> 연쇄적으로 발생하는 비동기 작업을 순차적으로 동작할 수 있게 함

### Promise

> Callback 작성할 때 마주하는 문제(가독성)를 해결하기 위해 등장한 비동기 처리를 위한 객체로 비동기 작업의 완료 또는 실패를 나타냄

- then(callback)
  
  - 요청한 작업이 성공하면 callback 실행
  
  - callback은 이전 작업의 성공 결과를 인자로 전달 받음

- catch(callback)
  
  - then()이 하나라도 실패하면 callback 실행
  
  - callback은 이전 작업의 실패 객체를 인자로 전달 받음

- then, catch는 모두 항상 promise 객체를 반환하여 chaining 할 수 있음
  
  - axios로 처리한 비동기 로직이 항상 promise 객체를 반환
