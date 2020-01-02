CREATE TABLE city (id serial, title text);
INSERT INTO city (title) VALUES('Kyev'),('Kharkiv'),('Lviv'),('Odessa'),('Dnepr'),('Zaporizhiya'),('Luzk');

CREATE TABLE users (id serial,gender varchar(1),name text,email text,city_id integer);
INSERT INTO users(gender,name,email,city_id) 
VALUES('m','Valera','Val@val.com',2), 
('m','Tommy','Tom@tomich.com',3),
('m','Tom','Tom@tomich.com',3),
('m','Donny','Don@tomich.com',3),
('m','Ron','Ron@tomich.com',3),
('m','Alex','Al@tomich.com',3),
('m','Dim','dim@tomich.com',3),
('m','Igogo','igogo@tomich.com',3),
('m','Step','step@tomich.com',3),
('m','Illi','illi@tomich.com',3),
('m','Toli','Toli@tomich.com',3),
('m','Van','Van@tomich.com',3),
('m','Vano','vanoooo@tomich.com',3),
('m','Serj','ser@tomich.com',3),
('m','Dani','dani@tomich.com',4),
('m','John','jojo@tomich.com',4),
('m','Oleh','ole@tomich.com',4),
('m','Ande','and@tomich.com',5),
('w','Dasha','dada@tomich.com',5),
('w','Masha','ma@tomich.com',5),
('w','Glasha','gla@tomich.com',5),
('w','Sasha','saha@tomich.com',5),
('w','Lana','lala@tomich.com',5),
('w','KaRa','kara@tomich.com',5),
('w','Taha','tata@tomich.com',5),
('w','Rita','rita@tomich.com',5),
('w','Rima','rima@tomich.com',5),
('w','Rusya','rusya@tomich.com',5),
('w','Marya','mari@tomich.com',5),
('w','Dasha','dada@tomich.com',5),
('w','DahaBraha','dabra@tomich.com',5),
('w','Dari','dari@tomich.com',6),
('w','Dasha','dada@tomich.com',6),
('w','Alexa','dada@tomich.com',7),
('w','Alena','dada@tomich.com',8),
('a','cat','cat@tomich.com',6);

--1 select names genders and emails
SELECT 
'This is '||name||', ' || CASE WHEN gender = 'm' THEN 'he' WHEN gender = 'w' THEN 'she' ELSE 'it' END ||' has email '||email as info
FROM users INNER JOIN city 
ON city.id = city_id;

--2 select cities with more than 10 users

SELECT title, COUNT(*) as cnt
FROM users FULL JOIN city
ON city.id = city_id
GROUP BY title HAVING COUNT(*) > 10
ORDER BY COUNT(*);