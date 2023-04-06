CREATE TABLE articles (
title TEXT,
content TEXT,
role INTEGER
);

CREATE TABLE users (
name TEXT,
role_id INTEGER
);

CREATE TABLE roles (
role TEXT
);

INSERT INTO articles VALUES
('제목1','내용1',1),
('제목2','내용2',2),
('제목3','내용3',3);
INSERT INTO users VALUES
('aiden',1),
('ken',3),
('lynda',3);
INSERT INTO roles VALUES
('admin'),
('staff'),
('student');

INSERT INTO articles VALUES
('제목4','내용4',4),
('제목5','내용5',5),
('제목6','내용6',6),
('제목7','내용7',7),
('제목8','내용8',8),
('제목9','내용9',9),
('제목10','내용10',10),
('제목11','내용11',11),
('제목12','내용12',12);

INSERT INTO users
VALUES
('sophia',2);

SELECT u.name, r.role 
FROM users AS u INNER JOIN roles as r
WHERE u.role_id = r.rowId;

/* 수강신청 db 구성해보기 */
TABLE 과목 (
과목코드 TEXT NOT NULL UNIQUE PK
과목명 TEXT NOT NULL
교수명 TEXT NOT NULL FK
강의시간 TEXT NOT NULL
);

TABLE 교수 (
rowid PK
교수명 TEXT NOT NULL
학과 TEXT NOT NULL
);

TABLE 학생 (