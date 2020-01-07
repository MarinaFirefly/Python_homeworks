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
                    (id serial, first_name text, last_name text, email text, 
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
            conn.close()
        else:
            print("Table with name {table} cannot be created!".format(table = self.table_name))

    def add_to_db(self,obj):
        conn = sqlite3.connect("employees.db")
        cursor = conn.cursor()
        try:
            if cursor.execute("SELECT * FROM {table_name}".format(table_name=self.table_name)):
                cursor.execute("SELECT COUNT(*) FROM {table}".format(table=self.table_name))
                num = cursor.fetchone()[0]+1
                val = ""
                if self.table_name == 'programmers':
                    obj = [(num,obj.first_name,obj.last_name,obj.email,obj.phone,obj.hired_at,
                        obj.salary_per_day,obj.main_skill,str(obj.data))]
                    val = "(?,?,?,?,?,?,?,?,?)"
                elif self.table_name == 'recruiters':
                    obj = [(num,obj.first_name,obj.last_name,obj.email,obj.phone,obj.hired_at,obj.salary_per_day)]
                    val = "(?,?,?,?,?,?,?)"
                elif self.table_name == 'candidates':
                    obj = [(num,obj.first_name,obj.last_name,obj.email,obj.phone,obj.main_skill)]
                    val = "(?,?,?,?,?,?,?)"
                elif self.table_name == 'vacancies':
                    obj = [(num,obj.title,obj.salary_per_day,obj.mail_skills,obj.technologies,
                        obj.recruiter,obj.hired_at,obj.status_of_vacancy)]
                    val = "(?,?,?,?,?,?,?)"
                elif self.table_name == 'iterviews':
                    obj = [(num,obj.vacancy,obj.programmer,obj.recruiter,obj.candidate,
                        obj.datetime_of_int,obj.feedback,obj.result)]
            
                cursor.executemany("INSERT INTO {table} VALUES {val}".format(table=self.table_name,val=val), obj)
                conn.commit()
                conn.close()
        except:
            print("Table with name {table} doesn't exist!".format(table = self.table_name))

    def read_from_db(self):
        conn = sqlite3.connect("employees.db")
        cursor = conn.cursor()
        try:
            if cursor.execute("SELECT * FROM {table_name}".format(table_name=self.table_name)):
                cursor.execute("SELECT * FROM {table_name}".format(table_name=self.table_name))
                print(cursor.fetchall())
        except:
            print("Table with name {table} doesn't exist!".format(table = self.table_name))

    def delete_from_db(self):
        conn = sqlite3.connect("employees.db")
        cursor = conn.cursor()
        try:
            cursor.execute("DROP TABLE {table_name}".format(table_name = self.table_name))
            conn.close()
        except:
            print("Table with name {table} doesn't exist!".format(table = self.table_name))


programmer_Ivan = Programmer("Ivan","Ivanov","ivan@gmail.com","12-12-12-1","02-10-12",50,"Java",tech_stack="[C++,Java,C#]",closed_this_month=2)
programmer_Ivan2 = Programmer("Ivan","Neivanov","ivan2@gmail.com","12-12-12-2","01-01-19",60,"C#",tech_stack="[C++,Java,C#,SQL]",closed_this_month=5)
programmer_Ivan3 = Programmer("Ivan","Neivanov","ivan3@gmail.com","12-12-12-2","01-01-19",70,"C#",tech_stack="[C++,Java,C#,SQL]",closed_this_month=7)

progs = ForTablesInDb("programmers")
progs.delete_from_db()
progs.create_table()
progs.add_to_db(programmer_Ivan)
progs.add_to_db(programmer_Ivan2)
progs.add_to_db(programmer_Ivan3)
progs.read_from_db()

recruiter_sema = Recruiter("Sema","Senov","sem@sem.gamil.com","12-111-11","12-12-18",90)
recrs = ForTablesInDb("recruiters")
recrs.add_to_db(recruiter_sema)