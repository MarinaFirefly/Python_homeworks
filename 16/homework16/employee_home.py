import datetime 


# Parent class (1 task)
class Employee:
    #in **data any additional information can be put (task 10)
    def __init__(self,name,email,phone,day_salary,**data):
        self.name = name
        self.email = email
        self.phone = phone
        self.day_salary = day_salary
        self.data = data
    #method work returns string "I come to the office." (task 2)

# function that returns amount of working days in the month without some hilidays
    def working_days(self):
        now = datetime.date.today()
        start_month = datetime.date(now.year,now.month,1)
        diff = (now - start_month).days + 1
        weekend = [5,6]
        holidays = [datetime.date(now.year,12,25),datetime.date(now.year,10,14),
            datetime.date(now.year,8,24),datetime.date(now.year,6,28),datetime.date(now.year,5,1)]
        working_days = 0
        for day in range(diff):
            if (start_month + datetime.timedelta(day)).weekday() not in weekend:
                working_days+=1
            if start_month + datetime.timedelta(day) in holidays:
                working_days-=1
        return working_days

    def work(self):
        return "I come to the office."
    #method check_salary returns salary for given amount of days (task 3)
    #if method is called without argument, working days from begging of the month are counted (task 8)
    def check_salary (self, days=None):
        if days == None:
            days = self.working_days()
        return "My salary is " + str(self.day_salary*days)


# class Recruiter is inherited from Employee (task 4)
class Recruiter(Employee):
    #method work is redefined (task 5)
    def work(self):
        return super().work().replace("."," and start hiring.")
    
    #method __str__ is redefined (task 6)
    def __str__(self):
        return "I'm recruiter " + self.name + "."
    
    # with this methods recruiters can be compared by the salaries (task 7)
    def __lt__(self,other):
        return self.day_salary < other.day_salary
    def __gt__(self,other):
        return self.day_salary > other.day_salary
    
    # adding of hired_this_month field (task 9)
    def set_hired_this_month(self,n):
        self.hired_this_month = n
    def get_hired_this_month(self):
        try:
            return "I hired " + str(self.hired_this_month) + " persons this month!"
        except:
            return "Nobody was hired this month!"


# class Programmer is inherited from Employee (task 4)
class Programmer(Employee):
    #method work is redefined (task 5)
    def work(self):
        return super().work()[:-1] + " and start coding."
    #method __str__ is redefined (task 6)
    def __str__(self):
        return "I'm programmer " + self.name + "."
    
    # with this methods programmers can be compared by their skills (task 11)
    def __gt__(self,other):
        return len(self.data.get("tech_stack")) > len(other.data.get("tech_stack"))
    def __lt__(self,other):
        return len(self.data.get("tech_stack")) < len(other.data.get("tech_stack"))
    def __eq__(self,other):
        return len(self.data.get("tech_stack")) == len(other.data.get("tech_stack"))

    #method that allows to get alpha programmer
    def __add__(self, other):
        prog = Programmer(None,None,None,0)
        prog.day_salary = self.day_salary + other.day_salary
        return prog


recurter_vasya = Recruiter("Vasya","vasiliy@gmail.com","23-23-234",200)
print(recurter_vasya)
print(recurter_vasya.work())
print(recurter_vasya.check_salary())

recurter_vanya = Recruiter("Vanya","vanaya@gmail.com","22-23-234",150)
print(recurter_vanya)
print(recurter_vanya.work())
print(recurter_vanya.check_salary(22))

programmer_Zhora = Programmer("Zhora","zhora@yahoo.com","12-12-122",200)
print(programmer_Zhora.work())
print(programmer_Zhora)
print(programmer_Zhora.check_salary(21))

if recurter_vasya < recurter_vanya:
    print ("Salary is lower!!!")
else: print ("Salary is not lower!")

if recurter_vasya > recurter_vanya:
    print ("Salary is higer!!!")
else: print ("Salary is not higher!")

recurter_valentin = Recruiter("Valentin","valik@gmail.com","1212121",170, hired_this_month = 10, notes = "get 5 seniors")
print(recurter_valentin.data.get("hired_this_month"))

programmer_Ivan = Programmer("Ivan","ivan@gmail.com","12-12-12-1",50,tech_stack="[C++,Java,C#]",closed_this_month=2)
programmer_Ivan2 = Programmer("Ivan","ivan2@gmail.com","12-12-12-2",60,tech_stack="[C++,Java,C#,SQL]",closed_this_month=5)

if programmer_Ivan > programmer_Ivan2:
    print ("More skills")
else: print ("Not more skills!")

print (recurter_vanya.get_hired_this_month())
recurter_vanya.set_hired_this_month('2')
print (recurter_vanya.get_hired_this_month())

print((programmer_Ivan + programmer_Ivan2).day_salary)
