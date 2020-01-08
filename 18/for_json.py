import json
import sqlite3

with open('data/db.json', 'r', encoding='utf-8') as f:
    data = json.load(f) 

for programmer in data["programmers"]:
    conn = sqlite3.connect("data/employees.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS programmers
                    (id serial, first_name text, last_name text, email text, 
                    phone text, hired_at text, salary_per_day integer, main_skill text,
                    additional_info text)""")
    cursor.execute("""INSERT INTO programmers
                    VALUES ('{id}','{first_name}','{last_name}','{email}','{phone}','{hired_at}','{salary_per_day}','{main_skill}','{data}')"""
                    .format(
                        id=programmer.get("id"),
                        first_name=programmer.get("first_name"),
                        last_name=programmer.get("last_name"),
                        email=programmer.get("email"),
                        phone=programmer.get("phone"),
                        hired_at=programmer.get("hired_at"),
                        salary_per_day=programmer.get("salary_per_day"),
                        main_skill=programmer.get("main_skill"),
                        data=programmer.get("additional_info")
                        ))
    conn.commit()
    conn.close()

for recruiter in data["recruiters"]:
    conn = sqlite3.connect("data/employees.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS recruiters
                    (id serial, first_name text, last_name text, email text, 
                    phone text, hired_at text, salary_per_day integer)""")
    cursor.execute("""INSERT INTO recruiters
                    VALUES ('{id}','{first_name}','{last_name}','{email}','{phone}','{hired_at}','{salary_per_day}')"""
                    .format(
                        id=recruiter.get("id"),
                        first_name=recruiter.get("first_name"),
                        last_name=recruiter.get("last_name"),
                        email=recruiter.get("email"),
                        phone=recruiter.get("phone"),
                        hired_at=recruiter.get("hired_at"),
                        salary_per_day=recruiter.get("salary_per_day"),
                        ))
    conn.commit()
    conn.close()

for candidate in data["candidates"]:
    conn = sqlite3.connect("data/employees.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS candidates
                    (id serial, first_name text, last_name text, email text, 
                    phone text, main_skill text)""")
    cursor.execute("""INSERT INTO candidates 
                    VALUES ('{id}','{first_name}','{last_name}','{email}','{phone}','{main_skill}')"""
                    .format(
                        id=candidate.get("id"),
                        first_name=candidate.get("first_name"),
                        last_name=candidate.get("last_name"),
                        email=candidate.get("email"),
                        phone=candidate.get("phone"),
                        main_skill=candidate.get("main_skill")
                        ))
    conn.commit()
    conn.close()

for vacancy in data["vacancies"]:
    conn = sqlite3.connect("data/employees.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS vacancies
                    (id serial, title text, salary_per_day integer, main_skills text, 
                    technoloies text, recruiter text, hired_at text, status_of_vacncy boolean)""")
    cursor.execute("""INSERT INTO vacancies
                    VALUES ({id},'{title}','{salary_per_day}','{main_skill}','{technologies}','{recruiter}','{hired_at}',{status})"""
                    .format(
                        id=vacancy.get("id"),
                        title=vacancy.get("title"),
                        salary_per_day=vacancy.get("salary_per_day"),
                        main_skill=vacancy.get("main_skill"),
                        technologies=vacancy.get("technologies"),
                        recruiter=vacancy.get("recruiter"),
                        hired_at=vacancy.get("hired_at"),
                        status=vacancy.get("status")
                        ))
    conn.commit()
    conn.close()

for interview in data["interviews"]:
    conn = sqlite3.connect("data/employees.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS interviews
                (id serial, vacancy text, programer text, recruiter text, 
                candidate text, datetime_of_int text, feedback text, result text)""")
    cursor.execute("""INSERT INTO interviews 
                    VALUES ({id},'{vacancy}','{programmer}','{recruiter}','{candidate}','{datetime}','{feedback}',{result})"""
                    .format(
                        id=interview.get("id"),
                        vacancy=interview.get("vacancy"),
                        programmer=interview.get("programmer"),
                        recruiter=interview.get("recruiter"),
                        candidate=interview.get("candidate"),
                        datetime=interview.get("datetime"),
                        feedback=interview.get("feedback"),
                        result=interview.get("result")
                        ))
    conn.commit()
    conn.close()