# Web

> 웹 페이지 구성요소 : HTML, CSS, JavaScript

- HTML : 구조

- HTML + CSS : 표현(Styling)

- HTML + CSS + JS : 동작(Interaction)

### HTML

> 웹 페이지의 구조, Hyper Text Markup Language
> 
> 도움되는 사이트 : mdn, w3schools

- Hyper Text
  
  - 참조(하이퍼링크)를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트

- Markup Language
  
  - 태그 등을 이용하여 문서나 데이터 구조를 명시하는 언어 (HTML, Markdown 등)
  
  - 예 : <p>

- 기본 구조
  
  - html : 문서의 최상위(root) 요소
  
  - head : 문서 메타데이터 요소
    
    - 문서 제목, 인코딩, 스타일, 외부 파일 로딩 등
    
    - 일반적으로 브라우저에 나타나지 않는 내용
    
    - 예시
      
      - <title> : 브라우저 상단 타이틀
      
      - <link> : 외부 리소스 연결 요소
      
      - <style> : css 직접 작성
      
      - 등
  
  - body : 문서 본문 요소
    
    - 실제 화면 구성과 관련된 내용

- 요소(element)
  
  - HTML의 요소는 태그와 내용으로 구성되어 있다.
    
    - 여는 태그, 내용, 닫는 태그
    
    - 태그는 그 정보의 성격과 의미를 정의
  
  - 중첩이 가능함

- 속성(attribute)
  
  - 각 태그별로 사용할 수 있는 속성이 다르며 속성명과 속성값으로 이루어짐
  
  - 태그의 부가적 정보 설정 가능
  
  - 요소는 속성을 가질 수 있으며 경로나 크기와 같은 추가적 정보 제공
  
  - 보통 이름과 값이 하나의 쌍으로 존재하며 요소의 시작 택에 작성함
  
  - 태그 상관없이 사용 가능한 속성도 있음
    
    - id, class, style 등

- 문서 구조화
  
  - 인라인 / 블록
  
  - 텍스트 요소
    
    - a, /a
      
      - href 속성을 활용하여 다른 url로 연결하는 하이퍼링크 생성
    
    - b, /b
    
    - i, /i
    
    - br
    
    - img
    
    - span, /span
  
  - form
    
    - 사용자의 정보(데이터)를 제출하기 위한 영역
  
  - input
    
    - 다양한 타입을 가지는 입력 데이터 유형과 위젯이 제공됨
    
    - input label을 통해 label에 input 초점을 맞추거나 활성화 시킬 수 있음
      
      - input에 id 속성을, label에 for 속성을 활용하여 상호 연관 시킴
    
    - type으로 HTML기본 검증 혹은 추가 속성을 활용할 수 있음
      
      - text : 일반 텍스트
      
      - password : 입력 시 값이 보이지 않고 문자를 특수기호(*)로 표현
      
      - email : 이메일 형식이 아닌 경우 form 제출 불가
      
      - number : min, max, step 속성 활용하여 숫자 범위 설정 가능
      
      - file : accept 속성 활용하여 파일 타입 지정 가능
      
      - 항목 중 선택
        
        - checkbox : 다중 선택
        
        - radio : 단일 선택

### CSS

> Cascading Style Sheets
> 
> 스타일을 지정하기 위한 언어
> 
> <link rel = "stylesheet" href=".css">
> 
> <link rel = "stylesheet" href=".css">

- 용어
  
  - 선택자
  
  - 선언
  
  - 속성
  
  - 값

- 정의 방법
  
  - 인라인
  
  - 내부 참조
  
  - 외부 참조

- 선택자 유형
  
  - 기본 선택자
    
    - 전체 선택자(*), 요소(tag) 선택자
    
    - 클래스 선택자, 아이디 선택자, 속성 선택자
  
  - 결합자
    
    - 자손 결합자, 자식 결합자

- 적용 우선순위
  
  - 중요도 - 사용시 주의
    
    - !important
  
  - **우선 순위**
    
    - 인라인 > id > class, 속성 > 요소

- CSS 상속
  
  - CSS는 상속을 통해 부모 요소의 속성을 자식에게 상속
    
    - 속정 중에는 상속이 되는 것과 돠지 않는 것들이 있다

- CSS 원칙
  
  - 모든 요소는 네모(박스모델)이고 위에서부터 아래로, 왼쪽에서 오른쪽으로 쌓인다
    (Normal Flow)

- Box model
  
  - 하나의 박스는 네 부분(영역)으로 이루어짐
    
    - content : 글이나 이미지 등 요소의 실제 내용
    
    - padding : 테두리 안쪽 내부 여백, 요소에 적용된 배경색, 이미지가 적용됨
    
    - border : 테두리 영역
    
    - margin : 테두리 바깥 외부 여백, 배경색 지정 불가
  
  - box의 width을 한번에 보고 싶을 때(content + padding의 width)
    box-sizing을 border-box으로 설정

- 개발자 도구
  
  - 크롬 등 웹 브라우저에서 제공하는 개발과 관련된 다양한 기능을 제공
    
    - 주요 기능
      
      - Elements - DOM 탐색 및 CSS 확인 및 변경
      
      - Styles - 요소에 적용된 CSS 확인
      
      - Computed - 스타일이 계산된 최종 결과
      
      - Event Listeners - 해당 요소에 적용된 이벤트 (JS)

- CSS Display
  
  - display에 따라 크기와 배치가 달라진다
    
    - div는 한 줄을 다 차지함
  
  - display : block
    
    - 줄 바꿈이 일어나는 요소 (다른 elem 밀어냄)
    
    - 화면 크기 전체의 가로 폭을 차지함
    
    - 블록 레벨 요소 안에 인라인 레벨 요소가 들어갈 수 있음
  
  - display : inline
    
    - 줄 바꿈이 일어나지 않는 행의 일부 요소
    
    - content 만큼만 차지함 (width, height, margin 지정 불가)
    
    - 상하 여백은 line-height로 지정
  
  - 블록 레벨 요소와 인라인 레벨 요소
    
    - 블록 레벨 : div / ul, ol, li / p / hr / form 등
    
    - 인라인 레벨 : span / a / img / input, label / b, em, i, strong
  
  - display : inline-block (안중요)
    
    - block과 inline 레벨 요소의 특징을 모두 가짐
    
    - inline처럼 한 줄에 표시 가능
  
  - display : none
    
    - 해당 요소를 화면에 표시하지 않고 공간 조차 부여되지 않음
    
    - 공간만 차지하기 - visibility : hidden;

- CSS Position
  
  - 문서 상에서 요소의 위치를 지정
    
    - static : 기본값
    
    - relative : 상대 위치(자기 자신의 static 위치 기준)
    
    - absolute : 절대 위치(요소를 일반 흐름에서 제거 후 레이아웃에 공간 차지 X) 
    
    - fixed : absolute와 같으나 부모 요소를 기준으로 삼지 않고 viewport가 기준
      (viewport : 화면(창)의 크기)
    
    - sticky : 스크롤에 따라 static ->  fixed로 변경

- CSS Layout
  
  - Float
  
  - Flexbox

### Bootstrap

- CDN
  
  - 컨텐츠(CSS, JS, Image, Text 등)를 효율적으로 전달하기 위해 여러 노드를 가진 네트워크에서 데이터를 제공하는 시스템

- 반응형 웹
  
  - Grid System
    
    - 편집 디자인에서 나온 개념으로 구성 요소를 잘 배치해서 시각적으로 좋은 결과물을 만들기 위함
    
    - 정보 구조와 배열을 체계적으로 작성하여 정보의 질서를 부여하는 시스템
    
    - 기본 요소
      
      - Column : 실제 컨텐츠를 포함하는 부분
      
      - Gutter : 칼럼과 칼럼 사이 공간 (사이 간격)
      
      - Container : 칼럼들을 담고 있는 공간
    
    - Bootstrap grid system에서 12개의 column, 6개의 grid breakpoints 기억
