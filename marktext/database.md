### 데이터베이스의 종류

- SQL 관계형 데이터베이스
  
  - 표 형식

- NoSQL 비관계형 데이터베이스 (No가 아닌 Not only)
  
  - 여러 형식

### SQL Commands 종류

- DDL 데이터 정의 언어
  
  - CREATE
  
  - DROP
  
  - ALTER

- DML 데이터 조작 언어
  
  - INSERT
  
  - SELECT
  
  - UPDATE
  
  - DELETE

- DCL 데이터 제어 언어
  
  - GRANT
  
  - REVOKE
  
  - COMMIT
  
  - ROLLBACK

### Constraints

> 제약조건, 입력하는 자료에 대해 제약을 정함
> 
> 데이터 무결성 (데이터에 대한 정확성과 일관성)을 위해 데이터 변경 혹은 수정 시 여러 제한을 두어 데이터의 정확성을 보증함

- 종류
  
  - NOT NULL
    
    - 칼럼이 NULL 값을 혀용하지 않도록 함
  
  - UNIQUE
    
    - 칼럼의 모든 값이 서로 구별되거나 고유한 값을 되도록 함
  
  - PRIMARY KEY
    
    - 행의 고유성을 식별하는 데 사용 (not null)
  
  - AUROINCREMENT
    
    - 사용되지 않은 값이나 이전에 삭제된 행 값 재사용 방지 (rowid)

### ALTER TABLE

- **Rename** a table

- **Rename** a column

- **Add** a new column to a table

- **Delete** a column

### Grouping data

- Aggregate function
  
  - AVG()
  
  - COUNT()
  
  - MAX()
  
  - MIN()
  
  - SUM()

- GROUP BY
  
  - 데이터들의 공통 값을 묶어서 결과를 나타내며 SELECT 문의 FROM 절 뒤에 작성
    
    - WHERE이 있으면 WHERE 절 뒤에 작성

### Changing data

- INSERT

- UPDATE

- DELETE

### 정규형

- 제 1정규형
  
  - 하나의 속성에는 값이 하나만 들어가야 함

- 제 2정규형
  
  - 테이블의 기본키에 종속되지 않는 칼럼은 테이블이 분리 되어야함

- 제 3정규형
  
  - 다른 속성에 의존(종속)하는 속성은 따로 분리할 것

- 더 있음

### JOIN

> 데이터를 합치는 함수

- CROSS JOIN
  
  - 모든 조합 출력

- INNER JOIN
  
  - 두 테이블에서 일치하는 데이터만 결과 출력

- LEFT JOIN
  
  - 왼쪽 테이블 데이터 기준으로 오른쪽 데이터 결합, 없으면 NULL

- RIGHT JOIN
  
  - 오른쪽 기준으로

- FULL OUTER JOIN



### 관계형 데이터베이스 (RDB)

> 데이터를 테이블, 행, 열 등으로 나누어 구조화하는 방식이며 모든 행에 고유하게 식별 가능한 기본 키라는 속성이 있다
> 
> 외래 키를 사용하여 서로 다른 테이브 간의 관계를 만들 수 있음

- 관계
  
  - 1:1 ex) 주문 - 송장
  
  - N:1 ex) 학생 - 강의
  
  - M:N ex) 가수 - 노래

### 외래 키 (FK)

> 관계형 데이터베이스에서 다른 테이블의 행을 식별할 수 있는 키
> 
> 값은 부모 테이블의 유일한 값이어야 함

### Django Relationship fields

- OneToOneField() 
  
  - 1:1

- ForeignKey()
  
  - N:1
  
  - 2개의 필수 위치 인자 필요
    
    - 참조하는 model class
    
    - on_delete 옵션
    
    - 외래 키가 참조하는 객체가 사라졌을 때 이 객체를 어떻게 처리할 지 정의함
    
    - related_name :  역참조시 사용하는 매니저 이름 설정

- ManyToManyField()
  
  - M:N

### 관계 모델 참조

- 정참조
  
  - 내가 갖고 있는 관계를 통해 참조함

- 역참조
  
  - 나를 참조하는 테이블을(나를 외래 키로 지정한 테이블) 참조하는 것

- Related manager
  
  - Django에서 N:1 , M:N 관계에서 사용 가능한 문맥이며 역참조할 수 있게 사용하는 manager 

### 유저 모델 참조

- settings.AUTH_USER_MODEL
  
  - **models.py의 모델 필드**에서 User 모델 참조할 때 사용

- get_user_model()
  
  - **models.py가 아닌 다른 모든 곳**에서 유저 모델을 참조할 때 사용
