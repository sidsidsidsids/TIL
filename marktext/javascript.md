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

### AJAX

> 비동기식 JavaScript와 XML, 비동기 통신 웹 개발 기술
> 
> 특징으로는 페이지 새로고침 없이 서버에 요청하며 서버로부터 응답 받아 작업을 수행한다


# Vue.JS

### Node.js

> 자바스크립트는 브라우저를 조작하는 유일한 어너지만 브라우저 밖에서 구동할 수 없었음
>
> 런타임 환경인 Node.js를 통해 브라우저가 아닌 환경에서도 구동할 수 있게 됨 

- NPM (Node Package Manage)

  - python에 pip가 있듯이 Node.js에는 npm이 있음
  
  - pip와 마찬가지로 다양한 의존성 패키지 관리

  - node_modules

    - node.js 환경의 여러 의존성 모듈로 python의 venv와 비슷한 역할을 함

      - .gitignore에 넣어줘야 하며 Vue 프로젝트를 생성하면 자동 생성됨

    - Babel

      - JavaScript의 ES6+ 코드를 구버전으로 번역/변환 해주는 도구

      - 브라우저 버전 별로 동작하지 않는 상황을 해결하기 위한 도구

    - Webpack

      - 모듈 간 의존성 문제를 해결하기 위한 도구

      - 프로젝트에 필요한 모든 모듈을 매핑하고 내부적으로 종속성 그래프를 빌드함

  - Module

    - 개발하는 애플리케이션의 크기가 커지고 복잡해지면 파일 하나에 모든 기능을 담기 어려워짐

    - 따라서 파일을 여러 개로 분리하여 관리하고 이때 분리된 파일 각각이 Module (js 파일 하나하나)
  
  - Bundler

    - 모듈 의존성 문제를 해결해주는 작업이 Bundling

    - Bundling된 결과물은 개별 모듈 실행 순서에 영향을 받지 않고 동작함

    - Vue CLI는 이러한 Babel, Webpack에 대한 초기 설정이 자동으로 되어 있음

  - package.json

    - 프로젝트의 종속성 목록과 지원되는 브라우저에 대한 구성 옵션 포함

  - package-lock.json

    - node_modules에 설치되는 모듈과 관련된 모든 의존성 설정 및 관리

    - python의 requirements.txt 역할

  - public/index.html
    
    - Vue 앱의 뼈대가 되는 html 파일이며 Vue 앱과 연결될 요소가 있음 

  - src/

    - src/assets

      - 정적 파일을 저장하는 디렉토리

    - src/components
      
      - 하위 컴포넌트들이 위치

    - src/App.vue

      - 최상위 컴포넌트

      - public/index.html과 연결됨

    - src/main.js

      - webpack이 빌드를 시작할 때 가장 먼저 불러오는 entry point

      - public/index.html과 src/App.vue를 연결시키는 작업이 이루어지는 곳
      
      - Vue 전역에서 활용 할 모듈을 등록할 수 있는 파일 

### Component

> UI를 독립적이고 재사용 가능한 조각들로 나눈 것
>
> CS에서는 다시 사용할 수 있는 범용성을 위해 개발된 소프트웨어 구성 요소를 의미
>
> 하나의 app을 구성할 때 중첩된 컴포넌트들의 tree로 구성하는 것이 보편적
> ex) Django : base.html - index.html 등 하나의 화면에 base가 들어가는 것 

- 특징

  - 관리 용이
  
  - 재사용성
  
  - 확장 가능

  - 캡슐화

  - 독립적

- component in Vue

  - Vue instance: new Vue()로 만든 인스턴스

  - SFC (Single File Component)
  
  - 구조

    - 탬플릿(HTML)

      - HTML의 body 부분, 눈으로 보여지는 요소

    - 스크립트(JavaScript)

      - JavaScript 코드가 작성되는 곳

      - 컴포넌트 정보, 데이터, 메서드 등 vue 인스턴스를 구성하는 대부분이 작성 됨

    - 스타일(CSS)

      - 컴포넌트의 스타일 담당

- data in components

  - 한 페이지 내에서 같은 데이터를 공유 해야함
  
  - 부모 자식 관계만 데이터를 주고받게 함으로써 유지 보수 및 흐름 파악 용이
  
  - 부모 -> 자식 : pass props / 자식 -> 부모 : emit event

- pass props

  - 요소의 속성(property)을 사용하여 데이터 전달

  - props는 부모 컴포넌트의 정보를 전달하기 위한 사용자 지정 특성

  - 자식 컴포넌트는 props 옵션을 사용하여 수신하는 props를 선언해야 함

  - prop-data-name="value"의 형태로 데이터를 전달

    - 부모에서 넘겨주는 props는 kebab-case (대소문자 구분 X)

    - 자식에서 받는 props는 camelCase

  - Dynamic props

    - v-bind directive를 사용해 데이터를 동적으로 바인딩

    - 부모 컴포넌트 데이터가 업데이트되면 자식 컴포넌트 데이터도 업데이트

- Emit Event

  - 부모 컴포넌트에서 자식 컴포넌트로 데이터를 전달할 때는 이벤트 발생

    - 데이터를 이벤트 리스너의 콜백함수 인자로 전달

    - 상위 컴포넌트는 해당 이벤트를 통해 데이터 받음

  - $emit('event-name') 형식으로 사용하여 부모 컴포넌트에 이벤트를 발생

  - Emit Event 흐름

    - 자식 컴포넌트의 이벤트를 청취하여 연결된 핸들러 함수(ChildToParent) 호출

    - 호출된 함수에서 $emit으로 상위 컴포넌트에 이벤트(child-to-parent) 발생

      - 이벤트에 데이터(child data)를 함께 전달

    - 상위 컴포넌트는 자식 컴포넌트의 이벤트를 청취하여 핸들러 함수(parentGetEvent) 호출

      - 함수의 인자로 전달된 데이터(child data)가 포함됨

- kebab-case와 camelCase 사용 케이스

  - HTML 요소에서 사용할 때는 kebab-case

  - JavaScript에서 사용할 때는 camelCase

  - in props

    - 상위 -> 하위 흐름에서 HTML 요소로 내려줌 : kebab-case

    - 하위에서 받을 때 JavaScript에서 받음 : camelCase

  - in emit

    - emit 이벤트를 발생시키면 HTML 요소가 이벤트를 청취 : kebab-case

    - 메서드, 변수명 등은 JavaScript 에서 사용함 : camelCase

- Lifecycle Hooks

  - Vue instance(컴포넌트)는 생성과 소멸의 과정 중 단계별 초기화 과정을 거침

    - Vue instance가 생성된 경우, 데이터 변경으로 DOM 업데이트하는 경우 등

  - 각 단계가 트리거가 되어 특정 로직을 실행할 수 있는데 이를 Lifecycle Hooks

  - instance마다 각각의 Lifecycle을 가지고 있음

  - 컴포넌트별로 정의할 수 있음

  - 부착 여부가 부모-자식 관계에 따라 순서를 가지고 있지 않음

  - 흐름

    - create

      - Vue instance가 생성된 후 호출되며 data, computed등 설정이 완료된 상태

      - mount되지 않아 요소에 접근할 수 없음

    - mount

      - Vue instance가 요소에 mount된 후 호출되며 요소를 조작할 수 있음

    - update

      - 데이터가 변경되어 DOM에 변화를 줄 때 호출됨

    - destruct

### Vuex

- State Management

  - 상태(State) : 현재에 대한 정보(data)

  - 여러 개의 component가 같은 상태(data)를 유지할 필요가 있음

  - Pass Props & Emit Event

    - 같은 데이터를 공유하고 있으므로 각 컴포넌트가 동일한 상태를 유지함

    - 중첩이 깊어지면 관리하기 힘들어짐 => 중앙 저장소에 데이터를 모아 상태 관리 (Vuex)

  - Vuex = 'state management pattern + library' for vue.js

    - 데이터가 에측 가능한 방식으로만 변경 되도록 규칙을 설정하며 반응성을 효율적으로 사용하게 관리

- Vuex

  - State

    - 중앙에서 관리하는 모든 상태 정보로 개별 component는 state에서 데이터를 가져와서 사용함

    - $store.state로 state 데이터에 접근함

  - Mutations

    - 실제로 state를 변경하는 유일한 방법이며 핸들러 함수는 반드시 동기적이어야 함

      - state 변화 시기를 특정하기 위함 (순서 처리)

    - 첫 인자로 state를 받으며 component 혹은 Actions에서 commit() 메서드로 호출됨

  - Actions

    - state를 변경하지 않고 commit() 메서드로 mutations를 호출해 state를 변경함

    - dispatch() 메서드로 호출됨

  - Getters

    - state를 활용하여 계산된 값을 얻고자 할 때 사용

    - 첫번째 인자로 state, 두번째 인자로 getter 받음

  - 데이터 흐름

    - component에서의 데이터 조작

      - component => (dispatch) -> actions => (commit) => mutations => state

    - component에서의 데이터 사용

      - state => (getter) => component

  - Local Storage

    - Window.localStorage

      - 브라우저 내장 객체 중 하나로 key-value 형태로 저장할 수 있는 저장소

      - localStorage에 저장된 데이터는 브라우저를 종료해도 유지 됨

      - setItem(key,value)

        - key, value 형태로 데이터 저장

      - getItem(key)

        - key 값으로 저장된 데이터 불러오기

      - JSON.stringify

        - 자바스크립트 객체를 JSON 형식의 문자열로 변환하여 반환

      - JSON.parse

        - JSON 형식의 문자열을 자바스크립트 객체로 변환하여 반환

      - vuex-persistedstate

        - vuex store의 상태를 브라우저 local storage에 저장해 주는 plugin

  - Vuex Binding Helper

    - Vuex store의 state, mutations, actions 등을 간단히 사용하기 위한 헬퍼

    - 사용하기 위해서는 import 받아와야 함

    - mapState

      - Vuex store의 상태를 컴포넌트 데이터에 객체, 배열 형태로 매핑할 때 사용

    - mapActions

      - this.$store.dispatch() 대신 액션 메서드를 직접 호출하여 사용 가능

    - mapGetters

      - 위 방식들과 동일하게 사용 가능

  - modules

    - Vuex store를 여러 파일로 나눠서 관리 할 수 있게 하는 기능

    - Store의 가독성 향상

- UX & UI

  - UX (User Experience)

    - 유저와 가장 가까이에 있는 분야로 개발자, 디자이너가 이해할 수 있게 소통

    - UX Researcher, User Researcher

  - UI (User Interface)

    - 유저에게 보여지는 화면을 디자인

    - Product Designer, Interaction Designer

  - Figma

    - Prototyping을 위한 Tool

    - **개발부터 시작하지 말고 반드시 충분한 기획을 거칠 것**

      - 화면, API 등 기획

- Vue Router

  - Routing

    - 네트워크에서 경로를 선택하는 프로세스

    - in SSR

      - Server가 모든 라우팅을 통제

    - in SPA/CSR

      - 서버는 하나의 HTML 만을 제공. 하나의 URL만 가질 수 있음

  - Vue Router

    - Vue의 공식 라우터로 SPA 상에서 라우팅을 쉽게 개발할 수 있는 기능 제공

    - 라우트에 컴포넌트를 매핑한 후 어떤 URL에서 렌더링 할지 알려줌

      - SPA의 단점 중 하나인 URL이 변경되지 않는다 를 해결함

    - router-link

      - a 태그와 비슷한 기능을 하여 URL을 이동시킴, 목표 경로는 'to' 속성으로 지정됨

    - router-view

      - 주어진 URL에 대해 일치하는 컴포넌트를 렌더링 하는 컴포넌트

    - History mode

      - 브라우저의 History API를 활용해 새로고침 없이 URL 이동 기록을 남길 수 있음

    - lazy-loading

      - 미리 로드를 하지 않고 특정 라우트에 방문할 때 매핑된 컴포넌트의 코드 로드 방식 사용 가능

        - 많이 쓰는 기능은 아님