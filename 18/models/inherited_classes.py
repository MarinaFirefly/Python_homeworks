import sqlite3
from .employee import Employee


class Programmer(Employee):
    # class Programmer is inherited from Employee
    def __init__(self,first_name,last_name,email,phone,hired_at,salary_per_day,main_skill,**data):
        super().__init__(first_name,last_name,email,phone)
        self.hired_at = hired_at
        self.salary_per_day = salary_per_day
        self.main_skill = main_skill
        self.data = data

    def work(self):
        #method work is redefined
        return super().work()[:-1] + " and start coding."
    def __str__(self):
        #method __str__ is redefined
        return "I'm programmer " + self.first_name + " " + self.last_name + "."
    
    def __gt__(self,other):
        # with this methods programmers can be compared by their skills
        return len(self.data.get("tech_stack")) > len(other.data.get("tech_stack"))
    def __lt__(self,other):
        return len(self.data.get("tech_stack")) < len(other.data.get("tech_stack"))
    def __eq__(self,other):
        return len(self.data.get("tech_stack")) == len(other.data.get("tech_stack"))

    def __add__(self,other):
        #method that allows to get alpha programmer
        return self.salary_per_day + other.salary_per_day

    def save_to_db(self):
        #add object to db
        conn = sqlite3.connect("data/employees.db")
        cursor = conn.cursor()
        try:
            #try will work if table exists in db
            if cursor.execute("SELECT * FROM programmers"):
                cursor.execute("SELECT COUNT(*) FROM programmers")
                id = cursor.fetchone()[0]+1 #count number of rows and make id bigger on 1
                obj = [(id,self.first_name,self.last_name,self.email,self.phone,self.hired_at,
                    self.salary_per_day,self.main_skill,str(self.data))]
                cursor.executemany("INSERT INTO programmers VALUES (?,?,?,?,?,?,?,?,?)", obj)
                conn.commit()
        except:
            print("Table with name {table} doesn't exist!".format(table = self.table_name))
        finally:
            conn.close()


class Recruiter(Employee):
    # class Recruiter is inherited from Employee
    def __init__(self,first_name,last_name,email,phone,hired_at,salary_per_day):
        super().__init__(first_name,last_name,email,phone)
        self.hired_at = hired_at
        self.salary_per_day = salary_per_day

    def work(self):
        #method work is redefined
        return super().work().replace("."," and start hiring.")
    
    def __str__(self):
        #method __str__ is redefined
        return "I'm recruiter " + self.first_name + " " + self.last_name + "."
    
    def __lt__(self,other):
        # with this methods recruiters can be compared by the salaries
        return self.salary_per_day < other.salary_per_day
    def __gt__(self,other):
        return self.salary_per_day > other.salary_per_day
    
    def set_hired_this_month(self,n):
        # adding of hired_this_month field 
        self.hired_this_month = n
    def get_hired_this_month(self):
        try:
            return "I hired " + str(self.hired_this_month) + " persons this month!"
        except:
            return "Nobody was hired this month!"


class Candidate(Employee):
    #in **data any additional information can be put
    def __init__(self,first_name,last_name,email,phone,main_skill):
        super().__init__(first_name,last_name,email,phone)
        self.main_skill = main_skill

    def work(self):
        raise TypeError