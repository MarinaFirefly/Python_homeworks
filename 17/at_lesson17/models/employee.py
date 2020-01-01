# Parent class 
class Employee:
    #in **data any additional information can be put
    def __init__(self,name,email,phone,day_salary,**data):
        self.name = name
        self.email = email
        self.phone = phone
        self.day_salary = day_salary
        self.data = data
    #method work returns string "I come to the office." 

# function that returns amount of working days in the month without some hilidays
    def working_days(self):
        import datetime
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
    #method check_salary returns salary for given amount of days
    #if method is called without argument, working days from begging of the month are counted
    def check_salary (self, days=None):
        if days == None:
            days = self.working_days()
        return "My salary is " + str(self.day_salary*days)
