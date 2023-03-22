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

### Design Pattern

> 소프트웨어도 자주 사용되는 구조와 해결책이 있다.
> 
> 클라이언트-서버 구조도 소프트웨어 디자인 패턴 중 하나

- 장점
  
  - 복잡한 커뮤니케이션이 매우 간단해짐

- Django에서의 Design Pattern
  
  - MTV Pattern
    
    - MVC Design Pattern을 조금 변형한 패턴
      
      - MVC : Model(데이터 관련 로직) - View(레이아웃과 화면) - Controller(명령을 Model과 View 부분으로 연결)
      
      - MVC의 목적 : 관심사를 분리하여 더 나은 업무 분리와 관리 제공 
        -> 유지보수 용이
    
    - MTV : Model - Template - View , MVC와 크게 다른 점은 없으며 부르는 이름이 다름
    
    - Model : MVC에서의 Model, 데이터 로직 관리 및 응용프로그램의 데이터 구조 정의와 데이터베이스 기록 관리
    
    - Template : MVC에서의 View, 레이아웃과 화면 처리, 화면상 사용자 인터페이스 구조와 레이아웃 정의
    
    - View : MVC에서의 Controller, Model & Template과 관련한 로직을 처리해서 응답을 반환하며 클라이언트의 요청에 대해 처리를 분기함

### Django Template

> 데이터 표현을 제어하는 도구이자 표현에 관련된 로직

- Django Template Language (DTL)
  
  - Django Template에서 사용하는 built-in template system
  
  - 단순히 Python이 HTML에 포함 된 것이 아니므로 주의
  
  - 프로그래밍적 로직이 아닌 프레젠테이션을 표현하기 위한 것

- DTL Syntax
  
  - Variable : 변수
    
    - 밑줄로는 시작 불가하며 공백이나 구두점 문자 또한 불가
    
    - dot(.) 이용하여 변수 속성 접근 가능
    
    - render()의 세번째 인자로 {'key':value}와 같이 dictionary 형태로 넘기며
      여기서 정의한 key에 해당하는 문자열이 template에서 사용 가능한 변수명임
  
  - Filters : 변수가 어떻게 보여질 지 조정
    
    - 표시할 변수를 수정할 때 사용하며 60개의 built-in template filters 제공
    
    - chained가 가능하며 일부 필터는 인자를 받기도 함
  
  - Tags : 기능
    
    - 출력 텍스트를 만들거나 반복 또는 논리를 수행하여 제어 흐름을 만드는 등 복잡한 일들을 수행
    
    - 일부 태그는 시작과 종료 태그가 필요함
    
    - 약 24개의 built-in template tags 제공
  
  - Comments : 주석
    
    - 한 줄 주석에만 사용할 수 있으며 유효하지 않은 템플릿 코드가 포함될 수 있음
    
    - 여러 줄 주석은 {% comment %}와 {% endcomment %} 사이에 입력

### Template inheritance

- 템플릿 상속
  
  - 기본적으로 코드의 재사용성에 초점을 맞춤
  
  - 태그를 이용하여 할 수 있음
    
    - 반드시 템플릿 최상단에 작성 되어야 함 (즉, 2개 이상 사용 불가)

### Trailing URL Slashes

- Django는 URL 끝에 /(Trailing slash)가 없다면 자동으로 붙이는 것이 기본 설정

### Variable routing

- URL 주소를 변수로 사용하는 것을 의미함

- 일부를 변수로 지정하여 view 함수의 인자로 넘길 수 있음
  
  - 따라서 변수 값에 따라 하나의 path()에 여러 페이지 연결할 수 있음

### App URL mapping

- urls.py를 쪼개어 각각의 app 폴더 안에 urls.py를 작성하여 매핑할 수 있다

### Form & Data

> Client & Server architecture

- HTML form
  
  - action
    
    - 입력 데이터가 전송될 URL 저장
    
    - 데이터를 어디로 보낼 것인지 지정, 지정하지 않으면 현재 form이 있는 페이지의 URL로 보내짐
  
  - method
    
    - 데이터를 어떻게 보낼 것인지 정의
    
    - HTML form 데이터를 GET 방식과 POST 방식으로 전송할 수 있음
  
  - HTML input elements
    
    - 사용자로부터 데이터를 입력 받기 위해 사용하며 'type' 속성에 따라 동작
      
      - MDN 문서 참고, 기본값은 text
    
    - name
      
      - form을 통해 데이터를 제출했을 때 name 속성에 설정된 값을 서버로 전송
      
      - 서버는 name 속성에 설정된 값을 통해 사용자가 입력한 데이터 값에 접근
      
      - 서버에 전달하는 param(key: name, value: value)로 매핑하는 것

- HTTP request methods
  
  - HTTP
    
    - HTML 문서와 같은 리소스들을 가져올 수 있도록 해주는 프로토콜
  
  - 자원에 대한 행위를 정의하며 주어진 자원에 수행하길 원하는 행동을 나타냄
  
  - GET
    
    - 서버로부터 정보를 조회하는 데 사용 (서버에게 리소스를 요청하기 위해 사용)
    
    - **데이터를 서버로 전송할 때 Query String Parameters를 통해 전송**
      
      - Query String Parameters
        
        - 사용자가 입력 데이터를 전달하는 방법 중 하나
        
        - 'key=value'로 필요한 파라미터 값을 적음 ( '='로 key와 value 구분 )
    
    - 데이터는 URL에 포함되어 서버로 보내짐

### Django Model

> Django는 웹 애플리케이션의 데이터를 구조화하고 조작하기 위한 추상적인 계층(모델)을 제공

- Database
  
  - 체계화된 데이터 모임
  
  - 검색 및 구조화 같은 작업을 쉽게 하기 위해 조직화 데이터를 수집하는 저장 시스템
  
  - 스키마(뼈대, 자료의 구조와 표현 방법과 관계 등을 정의한 구조)와
    테이블(데이터 요소들의 집합)로 이루어짐

- Django Model 개요
  
  - Django는 Model을 통해 데이터 접근 및 조작
  
  - 사용하는 데이터들의 필수적인 필드, 동작 포함
  
  - 저장된 데이터베이스의 구조
  
  - 모델 클래스 1개 == 데이터베이스 테이블 1개 (각 모델은 하나의 DB 테이블에 매핑)

### Migrations

> Django가 모델에 생긴 변화를 실제 DB에 반영하는 방법

- 주요명령어
  
  - makemigrations
    
    - 모델의 변경사항에 대한 새로운 migration을 만들 때 사용
  
  - migrate
    
    - makemigrations로 만든 설계도를 실제 DB에 반영하는 과정

- migration 3단계
  
  - models.py에 변경사항 발생
  
  - migration 생성 (makemigrations)
  
  - DB 반영 (migrate)

### ORM

> Object-Relational-Mapping
> 
> Django <-> DB 데이터 변환 프로그래밍 기술
> 
> SQL을 사용하지 않고 DB를 조작할 수 있게 함

- 특징
  
  - 장점
    
    - SQL을 몰라도 DB 조작 가능
    
    - 객체 지향적 접근으로 높은 생산성
  
  - 단점
    
    - 세밀한 DB 조작 구현 어려움

- 사용 이유 : 생산성이 뛰어남, DB를 객체로 조작

### QuerySet API

- Database API 구문
  
  - Model class . Manager . Queryset API 
    ex) Article.objects.all() 
  
  - objects manager
    
    - DB를 Python class로 조작할 수 있도록 여러 메서드를 제공하는 manager
  
  - query
    
    - 데이터베이스의 응답 데이터를 ORM이 QuerySet이라는 자료 형태로 변환하여 우리에게 전달함
  
  - QuerySet
    
    - 데이터베이스에게서 전달 받은 객체 목록
      
      - iterable 데이터
    
    - 복수가 아닌 단일 객체를 반환할 때에는 QuerySet가 아닌 Class가 반환됨

- CRUD
  
  - Create 생성
    
    - 첫번째 방법
      
      - article = Article()
        
        - 클래스를 통한 인스턴스 생성
      
      - article.title
        
        - 클래스 변수명과 같은 이름의 인스턴스 변수를 생성 후 값 할당
      
      - article.save()
        
        - 인스턴스로 save 메서드 호출
    
    - 두번째 방법
      
      - Article.objects.create()
  
  - Read 조회
    
    - all()
      
      - 전체 데이터 조회
    
    - get()
      
      - 단일 데이터 조회
      
      - 둘 이상 찾으면 예외를 발생시켜 고유성을 보장할 때 사용해야 함
    
    - filter()
      
      - 조회 매개 변수와 일치하는 객체를 포함하는 새 QuerySet 반환
      
      - Field lookups
  
  - Update 수정
    
    - 수정하고자 하는 article 인스턴스 객체 조회 후 반환 값 저장
    
    - article 인스턴스 객체 인스턴스 변수 값 새 값으로 할당
    
    - save() 인스턴스 메서드 호출
  
  - Delete 삭제
    
    - 삭제하고자 하는 article 인스턴스 객체 조회 후 반환 값 저장
    
    - delete() 인스턴스 메서드 호출

### Admin site

### CRUD with View

- ```shell
  $ python manage.py shell
  Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
  Type "help", "copyright", "credits" or "license" for more information.
  (InteractiveConsole)
  >>> from articles.models import Article
  >>> Article.objects.all()
  <QuerySet [<Article: 1번째 글 - 1>, <Article: 2번째 글 - 2>, <Article: 3번째 글 - 3>]>
  >>> exit()       
  (venv) 
  SSAFY@DESKTOP-DOGVPUB MINGW64 ~/Desktop/django_p
  $ py manage.py shell
  Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
  Type "help", "copyright", "credits" or "license" for more information.
  (InteractiveConsole)
  >>> from articles.models import Article
  >>> article = Article.objects.get(id=2)
  >>> article
  <Article: 2번째 글 - 2>
  >>> Article.objects.create(title='4번', content='4')
  <Article: 4번째 글 - 4번>
  >>> Articles.objects.all()
  Traceback (most recent call last):
    File "<console>", line 1, in <module>
  NameError: name 'Articles' is not defined
  >>> Article.objects.all()
  <QuerySet [<Article: 1번째 글 - 1>, <Article: 2번째 글 - 2>, <Article: 3번째 글 - 3>, <Article: 4번
  째 글 - 4번>]>
  >>> article = Article.objects.get(id=4)
  >>> article.title = "쉬는시간?"
  >>> article.save()
  >>> Article.objects.all()
  <QuerySet [<Article: 1번째 글 - 1>, <Article: 2번째 글 - 2>, <Article: 3번째 글 - 3>, <Article: 4번
  째 글 - 쉬는시간?>]>
  >>> article.delete()
  (1, {'articles.Article': 1})
  >>> Article.objects.all()
  <QuerySet [<Article: 1번째 글 - 1>, <Article: 2번째 글 - 2>, <Article: 3번째 글 - 3>]>
  ```

### Django Form

- Form 클래스를 선언하여 사용
  
  - Model과 마찬가지로 상속을 통해 선언 (forms 라이브러리의 Form 클래스 상속)
  
  - 앱 폴더에 forms.py 생성 후 ArticleForm Class 선언
  
  - as_p(), as_ul(), as_table() 등으로 각 필드를 감쌀 방법 선택

- HTML input 요소 표현
  
  - Form fields (ex. form.CharField())
    
    - 입력에 대한 유효성 검사 로직을 처리하며 탬플릿에서 직접 사용됨
  
  - Widgets (ex.forms.CharField(widget=forms.Textarea))
    
    - 웹 페이지의 요소 렌더링을 담당하며 단순 input 요소의 보여지는 부분 변경

### Django ModelForm

### Static & Media Files

- Static File
  
  - 파일 자체가 고정되어 있고 서비스 중에도 추가되거나 변경되지 않는 파일

- Media File
  
  - 사용자가 웹에서 업로드하는 정적 파일

- 웹 서버의 기본 동작
  
  - 특정 위치(URL)에 있는 자원을 요청(HTTP request)받아 응답(HTTP response)하고 제공하는 것
  
  - 이는 자원과 자원에 접근 가능한 주소가 있음을 의미
    
    - 예) 사진 파일은 자원이고 해당 사진 파일을 얻기 위한 경로인 웹 주소(URL)가 존재함

- Static file 구성
  
  - INSTALLED_APPS에 django.contrib.staticfiles 포함 확인
  
  - settungs.py에서 STATIC_URL 정의
  
  - 앱의 static 폴더에 정적 파일 위치하기
  
  - 템플릿에서 static 템플릿 태그 사용하여 지정된 경로에 있는 정적 파일 URL 만들기
  
  - 관련 Settings
    
    - STATIC_ROOT
      
      - 배포할 때 사용
    
    - STATICFILES_DIRS
      
      - 추가적인 정적 파일 경로 목록 정의
    
    - **STATIC_URL**
      
      - URL 경로 지정

- Media file 구성

### 인증과 권한

> 인증 시스템 (Django authentication system)은 인증과 권한 부여를 함께 제공하며 이러한 기능을 일반적으로 인증 시스템이라고 함

- 사전 설정

- DB 초기화(수동)
  
  - migrations 파일 삭제
    
    - migrations 폴더 및 init.py는 삭제하지 않음
  
  - db.sqlite3 삭제
  
  - migrations 진행
    
    - makemigrations
    
    - migrate

- HTTP
  
  - 특징
    
    - 비 연결 지향
      
      - 서버는 요청에 대한 응답을 보낸 후 연결을 끊음
        
        - ex) 네이버 메인 페이지를 보고 있을 때 네이버 서버와 연결되있지 않음
        
        - 네이버 서버는 우리에게 메인 페이지를 응답하고 연결을 끊은 것
    
    - 무상태
      
      - 연결을 끊는 순간 클라이언트와 서버 간 통신이 끝나며 상태 정보 유지 X
    
    - 서버와 지속적 연결을 위해 쿠키와 세션 존재
  
  - 쿠키
    
    - HTTP 쿠키는 상태가 있는 세션을 만들도록 해 줌
    
    - 두 요청이 동일한 브라우저에서 들어왔는지 아닌지를 판단할 때 사용
      
      - 이를 이용해 로그인 상태 유지 가능(무상태 HTTP 프로토콜에서 상태 정보를 기억 시켜 주기 때문)
    
    - 수명
      
      - session cookie
        
        - 현재 세션이 종료되면 삭제됨(브라우저 종료와 함께 삭제됨)
      
      - persistent cookie
        
        - 지정된 기간이 지나면 삭제됨
  
  - 세션
    
    - 사이트와 특정 브라우저 사이의 상태를 유지시키는 것
    
    - 클라이언트가 서버에 접속하면 서버가 특정 **session id**를 발급하고 클라이언트는 이를 쿠키에 저장
      
      - 클라이언트가 다시 동일 서버에 접속하면 요청과 함께 쿠키를 서버에 전달
      
      - 서버에서 session id를 확인해 알맞은 로직을 처리
    
    - 세션을 구별하기 위해 session id 필요
  
  - 로그인
    
    - Session을 create하는 과정
    
    - AuthenticationForm
      
      - 로그인을 위한 built-in form
      
      - request를 첫번째 인자로 취함
    
    - ```python
      from django.contrib.auth import login as auth_login
      ```
  
  - 로그아웃
    
    - Session을 delete하는 과정
      
      - 현재 요청에 대한 session data를 DB에서 삭제
      
      - 클라이언트 쿠키에서 session ID 삭제
    
    - ```python
      from django.contrib.auth import logout as auth_logout
      ```
