# Django

> 웹 서비스 개발에 필요한 로그인/아웃, 회원관리, DB, 서버 등 너무 많은 기술들이 필요하지만 잘 만들어진 것들을 가져다 잘 쓰기만 하면 됨

- Framework
  
  - 서비스 개발에 필요한 기능들을 미리 구현해서 모아 놓은 것
  
  - 웹 개발에 있어 모든 것들을 직접 개발할 필요 없이 본질에 집중할 수 있음
  
  - Django도 이러한 Framework중 하나

- Django를 배우는 이유
  
  - Python으로 작성됨
  
  - 수많은 유용한 기능
  
  - 검증됨 (화해, Toss, 두나무, 당근, 요기요 등이 사용 중)

- Django VS spring
  
  - Django는 독선적, 올바르게 사용하기 위한 메뉴얼이 존재
  
  - springboot는 관용적

- 코드 작성 순서
  
  1. urls.py
  
  2. views.py
  
  3. templates

### 클라이언트와 서버

> 대부분의 웹 서비스는 클라이언트-서버 구조
> 
> 클라이언트와 서버 역시 하나의 컴퓨터이다

- 클라이언트
  
  - 웹 사용자 인터넷에 연결된 장치
  
  - Chrome 또는 Firefox와 같은 웹 브라우저
  
  - 서비스를 요청하는 주체

- 서버
  
  - 요청에 대해 서비스를 응답하는 주체
  
  - Django는 서버를 구현하는 웹 프레임워크

### 가상환경

> 각각의 패키지를 하나의 환경에 담아야 한다면?
> 
> 프로젝트별 패키지를 독립적으로 관리하기 위한 것

- 가상환경 생성
  
  - python -m venv venv

- 가상환경 활성화(ON)
  
  - source venv/Scripts/activate

- 가상환경 비활성화(OFF)
  
  - deactivate

- 가상환경 패키지 목록 저장
  
  - pip freeze > requirements.txt

- 파일로부터 패키지 설치
  
  - pip install -r requirements.txt

### 프로젝트와 앱

- 프로젝트 만들기
  
  - django-admin startproject 프로젝트이름 (.)
    
    - .을 넣으면 manage.py가 현재 열린 폴더에, 넣지 않으면 프로젝트 안에 생성됨

- 프로젝트 구조
  
  - init.py
    
    - python에게 이 디렉토리를 하나의 python 패키지로 다루도록 지시
  
  - asgi.py
    
    - Django 애플리케이션이 비동기식 웹 서버와 연결 및 소통하는 걸 도움
  
  - **settings.py**
    
    - Django 프로젝트 설정을 관리
  
  - urls.py
    
    - 사이트 url과 적절한 views의 연결 지정
  
  - wsgi.py
    
    - 웹서버 연결 및 소통을 도움
  
  - manage.py
    
    - Django 프로젝트와 다양한 방법으로 상호작용 하는 커맨드라인 유틸리티

- Django Application
  
  - 앱 생성
    
    - $ python manage.py startapp articles
  
  - 앱
    
    - 하나의 큰 기능 단위
    
    - 정해진 규칙은 없으며 개발자가 판단하여 앱 생성

- 앱 구조
  
  - admin.py
    
    - 관리자용 페이지를 설정하는 곳
  
  - apps.py
    
    - 앱의 정보가 작성된 곳
  
  - **models.py**
    
    - 애플리케이션에서 사용하는 Model을 정의하는 곳
  
  - tests.py
    
    - 프로젝트 테스트 코드를 작성하는 곳
  
  - views.py
    
    - view 함수들이 정의 되는 곳

- 앱 등록
  
  - 사용하기 위해서는 INSTALLED_APPS 리스트에 반드시 추가해야 함

### 요청과 응답

> Django의 세 가지 구조 : Model, View, Template

- URLs
  
  - 
