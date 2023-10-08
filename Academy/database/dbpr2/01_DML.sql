-- users table 생성
CREATE TABLE users (
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    country TEXT NOT NULL,
    phone TEXT NOT NULL,
    balance INTEGER NOT NULL
);

SELECT last_name, count(*) as cnt 
FROM users GROUP BY last_name
ORDER BY cnt desc;

CREATE TABLE classmates (
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    address TEXT NOT NULL
);

INSERT INTO classmates
VALUES ('홍길동',23,'서울');

INSERT INTO classmates
VALUES
('김철수',30,'경기'),
('이영미',31,'강원'),
('박진성',26,'전라'),
('최지수',12,'충청'),
('중요한',28,'경상');

UPDATE classmates
SET name = "두루", address = "제주"
WHERE rowid=2;

DELETE FROM classmates
WHERE rowid=6;