--Create db for salary of population

CREATE DATABASE population;
\c population;

--Create table for regions
CREATE TABLE regions (id serial, region text, index integer);
INSERT INTO regions (region,index)
VALUES ('Kyev',01001),('Lviv',79000),('Odessa',65000),('Kharkiv',61000),('Dnepr',69000);

--forgot column with average salary
ALTER TABLE REGIONS ADD COLUMN average_salary numeric;
UPDATE regions SET average_salary = 20000 WHERE id=1;
UPDATE regions SET average_salary = 15000 WHERE id=2;
UPDATE regions SET average_salary = 17000 WHERE id=3;
UPDATE regions SET average_salary = 19000 WHERE id=4;
UPDATE regions SET average_salary = 14000 WHERE id=5;
SELECT * FROM regions;

--create table for persons
CREATE TABLE personal_salary (id serial, first_name text, last_name text, salary numeric, gender text);

INSERT INTO personal_salary (first_name,last_name,salary,gender)
VALUES ('Gosha', 'Petechkin', 12000, 'm'),
('Larisa','Zhukina',10000,'f'),
('Vasyliy','Plaksij', 7000,'m'),
('Dasha','Nashina',30000,'f'),
('Lubov','Fateeva', 5000, 'f'),
('Alex','Nealex', 21000,'m'),
('Vlad','Kuleshov', 19000,'m'),
('Ruslan','Nosov', 35000,'m'),
('Anzhela','Drova', 9000,'f');

--forgot column regions :(
ALTER TABLE personal_salary ADD COLUMN region text DEFAULT 'Kyev';
UPDATE personal_salary SET region = 'Kharkiv' WHERE id=2 or id=5;
UPDATE personal_salary SET region = 'Poltava' WHERE id=3 or id=6;
UPDATE personal_salary SET region = 'Dnepr' WHERE id=4;
UPDATE personal_salary SET region = 'Lviv' WHERE id=9; 

--inner join
SELECT * 
FROM personal_salary 
INNER JOIN regions 
ON personal_salary.region = regions.region;

--full join with renamed filed
SELECT 
    last_name || ' ' || upper(left(first_name,1)) || '.' as name,
    gender,
    personal_salary.region,
    average_salary
FROM personal_salary 
FULL JOIN regions 
ON personal_salary.region = regions.region
ORDER by name;     

--full join with condition count rows with some empty fields
SELECT 
    COUNT(*),
    personal_salary.region as person_region
FROM personal_salary 
FULL JOIN regions 
ON personal_salary.region = regions.region
WHERE personal_salary.region IS NULL OR regions.region IS NULL
GROUP by personal_salary.region;  

--left join to see salary more than average
SELECT 
   first_name || ' ' || last_name as name,
   salary,
   salary - average_salary as salary_diff
FROM personal_salary 
LEFT JOIN regions 
ON personal_salary.region = regions.region
WHERE salary > average_salary;   

--right join to see city that hasn't entries and average_salary in it
SELECT 
   regions.region,
   average_salary
FROM personal_salary 
RIGHT JOIN regions 
ON personal_salary.region = regions.region
WHERE personal_salary.region IS NULL;   