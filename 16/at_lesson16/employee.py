import datetime 
#
def working_days():
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

class Employee:
    def __init__(self,name,email,phone,day_salary,**data):
        self.name = name
        self.email = email
        self.phone = phone
        self.day_salary = day_salary
        self.data = data
    
    def work(self):
        return "I come to the office."

    def check_salary (self, days=None):
        if days == None:
            days = working_days()
        return self.day_salary*days


class Recurter(Employee):
    def work(self):
        return super().work().replace("."," and start hiring.")
    def __str__(self):
        return "I'm recruiter " + self.name + "."
    def __lt__(self,other):
        return self.day_salary < other.day_salary
    def __gt__(self,other):
        return self.day_salary > other.day_salary

class Programmer(Employee):
    def work(self):
        return super().work()[:-1] + " and start coding."
    def __str__(self):
        return "I'm programmer " + self.name + "."
    def __gt__(self,other):
        return len(self.data.get("tech_stack")) > len(other.data.get("tech_stack"))
    


recurter_vasya = Recurter("Vasya","vasiliy@gmail.com","23-23-234",200)
print(recurter_vasya)
print(recurter_vasya.work())
print(recurter_vasya.check_salary())

recurter_vanya = Recurter("Vanya","vanaya@gmail.com","22-23-234",150)
print(recurter_vasya)
print(recurter_vasya.work())
print(recurter_vasya.check_salary(22))

programmer_Zhora = Programmer("Zhora","zhora@yahoo.com","12-12-122",200)
print(programmer_Zhora.work())
print(programmer_Zhora)
print(programmer_Zhora.check_salary(21))

if recurter_vasya < recurter_vanya:
    print ("Lower!!!")
else: print ("Not lower!")

if recurter_vasya > recurter_vanya:
    print ("Higer!!!")
else: print ("Not higher!")

recurter_valentin = Recurter("Valentin","valik@gmail.com","1212121",170, hired_this_month = 10, notes = "get 5 seniors")
print(recurter_valentin.data.get("hired_this_month"))

programmer_Ivan = Programmer("Ivan","ivan@gmail.com","12-12-12-1",50,tech_stack="[C++,Java,C#]",closed_this_month=2)
programmer_Ivan2 = Programmer("Ivan","ivan2@gmail.com","12-12-12-2",60,tech_stack="[C++,Java,C#,SQL]",closed_this_month=5)

if programmer_Ivan > programmer_Ivan2:
    print ("More skills")
else: print ("Not more skills!")

#magic methods
#__lt__ - lower
#__gt__ - greater
#__eq__ - equal
#__le__ - lower or equal
#__ge__ - greater or equal 
#__neq__ - not equal
