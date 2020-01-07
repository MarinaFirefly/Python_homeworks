import sqlite3
from models.inherited_classes import Programmer
from models.inherited_classes import Recruiter
from models.inherited_classes import Candidate
from models.vacancy import Vacancy
from models.interview import Interview


class ForTablesInDb:
    def __init__(self,table_name):
        self.table_name = table_name

    def create_table(self):
        if self.table_name in ['programmers','recruiters','candidates','vacancies','iterviews']:
            fields = ''

            if self.table_name == 'programmers':
                fields = """CREATE TABLE IF NOT EXISTS programmers
                    (id serial, first_name text, last_name text, email text, 
                    phone text, hired_at text, salary_per_day integer, main_skill text,
                    additional_info text)"""
            elif self.table_name == 'recruiters':
                fields = """CREATE TABLE IF NOT EXISTS recruiters
                    (id seriabl, first_name text, last_name text, email text, 
                    phone text, hired_at text, salary_per_day integer)"""
            elif self.table_name == 'candidates':
                fields = """CREATE TABLE IF NOT EXISTS candidates
                    (id serial, first_name text, last_name text, email text, 
                    phone text, main_skill text)"""
            elif self.table_name == 'vacancies':
                fields = """CREATE TABLE IF NOT EXISTS vacancies
                    (id serial, title text, salary_per_day integer, main_skills text, 
                    technoloies text, recruiter text, hired_at text, status_of_vacncy boolean)"""
            elif self.table_name == 'iterviews':
                fields = """CREATE TABLE IF NOT EXISTS iterviews
                (id serial, vacancy text, programer text, recruiter text, 
                candidate text, datetime_of_int text, feedback text, result text)"""
            
            conn = sqlite3.connect("employees.db")
            cursor = conn.cursor()
            cursor.execute(fields)
        else:
            print("Table with name {table} cannot be created!".format(table = self.table_name))

    def add_to_db(self):
        if self.table_name in ['programmers','recruiters','candidates','vacancies','iterviews']:
            conn = sqlite3.connect("employees.db")
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM self.table_name")
            num = cursor.fetchone()[0]+1

            if self.table_name == 'programmers':
                fields = """CREATE TABLE IF NOT EXISTS programmers
                    (id serial, first_name text, last_name text, email text, 
                    phone text, hired_at text, salary_per_day integer, main_skill text,
                    additional_info text)"""
            elif self.table_name == 'recruiters':
                fields = """CREATE TABLE IF NOT EXISTS recruiters
                    (id seriabl, first_name text, last_name text, email text, 
                    phone text, hired_at text, salary_per_day integer)"""
            elif self.table_name == 'candidates':
                fields = """CREATE TABLE IF NOT EXISTS candidates
                    (id serial, first_name text, last_name text, email text, 
                    phone text, main_skill text)"""
            elif self.table_name == 'vacancies':
                fields = """CREATE TABLE IF NOT EXISTS vacancies
                    (id serial, title text, salary_per_day integer, main_skills text, 
                    technoloies text, recruiter text, hired_at text, status_of_vacncy boolean)"""
            elif self.table_name == 'iterviews':
                fields = """CREATE TABLE IF NOT EXISTS iterviews
                (id serial, vacancy text, programer text, recruiter text, 
                candidate text, datetime_of_int text, feedback text, result text)"""
            
            conn = sqlite3.connect("employees.db")
            cursor = conn.cursor()
            cursor.execute(fields)
        else:
            print("Table with name {table} cannot be created!".format(table = self.table_name))

            cursor.execute("SELECT COUNT(*) FROM self.table_name")
            num = cursor.fetchone()[0]+1


conn = sqlite3.connect("employees.db")
cursor = conn.cursor()

def create_programmers_table():
    cursor.execute("""CREATE TABLE IF NOT EXISTS programmers
                (id serial, first_name text, last_name text, email text, 
                phone text, hired_at text, salary_per_day integer, main_skill text,
                additional_info text)""")

def create_recruiters_table():
    cursor.execute("""CREATE TABLE IF NOT EXISTS recruiters
                (id serial, first_name text, last_name text, email text, 
                phone text, hired_at text, salary_per_day integer)""")

def create_candidates_table():
    cursor.execute("""CREATE TABLE IF NOT EXISTS candidates
                (id serial, first_name text, last_name text, email text, 
                phone text, main_skill text)""")

def create_vacancies_table():
    cursor.execute("""CREATE TABLE IF NOT EXISTS vacancies
                (id serial, title text, salary_per_day integer, main_skills text, 
                technoloies text, recruiter text, hired_at text, status_of_vacncy boolean)""")

def create_iterviews_table():
    cursor.execute("""CREATE TABLE IF NOT EXISTS iterviews
                (id serial, vacancy text, programer text, recruiter text, 
                candidate text, datetime_of_int text, feedback text, result text)""")

def add_programmer_to_db(programmer):
    cursor.execute("SELECT COUNT(*) FROM programmers")
    num = cursor.fetchone()[0]+1
    programmer = [(num,programmer.first_name,programmer.last_name,programmer.email,
                programmer.phone,programmer.hired_at,programmer.salary_per_day,
                programmer.main_skill, str(programmer.data))]
    cursor.executemany("INSERT INTO programmers VALUES (?,?,?,?,?,?,?,?,?)", programmer)
    conn.commit()


programmer_Ivan = Programmer("Ivan","Ivanov","ivan@gmail.com","12-12-12-1","02-10-12",50,"Java",tech_stack="[C++,Java,C#]",closed_this_month=2)
programmer_Ivan2 = Programmer("Ivan","Neivanov","ivan2@gmail.com","12-12-12-2","01-01-19",60,"C#",tech_stack="[C++,Java,C#,SQL]",closed_this_month=5)
programmer_Ivan3 = Programmer("Ivan","Neivanov","ivan3@gmail.com","12-12-12-2","01-01-19",70,"C#",tech_stack="[C++,Java,C#,SQL]",closed_this_month=7)

create_programmers_table()
add_programmer_to_db(programmer_Ivan)
add_programmer_to_db(programmer_Ivan2)
add_programmer_to_db(programmer_Ivan3)


