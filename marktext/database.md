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


