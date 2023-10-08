CREATE TABLE users (
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  age INTEGER NOT NULL,
  country TEXT NOT NULL,
  phone TEXT NOT NULL,
  balance INTEGER NOT NULL
);

SELECT first_name, age FROM users;

SELECT rowid, first_name from users;

SELECT first_name, age FROM users ORDER BY age;

SELECT first_name, age, balance FROM users ORDER BY age, balance desc;

SELECT country, COUNT(*) as numbers, AVG(age) FROM users GROUP BY country ORDER BY numbers desc;

SELECT first_name, age, balance FROM users WHERE age < 20 AND balance > 100000;

SELECT first_name,last_name FROM users WHERE first_name LIKE '%준';

SELECT last_name,first_name FROM users ORDER BY balance desc LIMIT 10;