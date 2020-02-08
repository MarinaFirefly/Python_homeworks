from .employee import Employee

# class Recruiter is inherited from Employee
class Recruiter(Employee):
    #method work is redefined (task 5)
    def work(self):
        return super().work().replace("."," and start hiring.")
    
    #method __str__ is redefined
    def __str__(self):
        return "I'm recruiter " + self.name + "."
    
    # with this methods recruiters can be compared by the salaries
    def __lt__(self,other):
        return self.day_salary < other.day_salary
    def __gt__(self,other):
        return self.day_salary > other.day_salary
    
    # adding of hired_this_month field 
    def set_hired_this_month(self,n):
        self.hired_this_month = n
    def get_hired_this_month(self):
        try:
            return "I hired " + str(self.hired_this_month) + " persons this month!"
        except:
            return "Nobody was hired this month!"