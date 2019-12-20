#Parent class
class Employee:
    days_of_vacation = 24
    salary_min = 300
#counts salary if omeovertime is. Overtime must be entered in percents.
    def salary_counter (self,perc_overtime,salary):
        if salary == "":
            salary = self.salary_min
        return salary + perc_overtime*salary/100
#counts how many days of vacation should employee has
    def days_of_vacation_counter(self,work_with_PC,few_childs):
        days_of_vacation = self.days_of_vacation
        if work_with_PC == True:
            days_of_vacation +=4
        if few_childs == True:
            days_of_vacation += 10
        return days_of_vacation

class Recruter(Employee):
    #some starter salaries for further calculations
    salary_junior = 300
    salary_middle = 700
    salary_senior = 1500
    #counts bonuses
    def bonus_counter(self,position,qauntity_empl):
        bonus = 0
        if position == "junior":
            salary = self.salary_junior
        elif position == "middle":
            salary = self.salary_middle
        elif position == "senior":
            salary = self.salary_middle
        else:
            salary = self.salary_min

        if qauntity_empl > 10:
            bonus += salary*0.3
        return bonus

class Technical(Employee):
    #some starter salaries for further calculations
    salary_junior = 400
    salary_middle = 1000
    salary_senior = 2500
    #counts bonuses
    def bonus_counter(self,position,qauntity_projects):
        bonus = 0
        if position == "junior":
            salary = self.salary_junior
        elif position == "middle":
            salary = self.salary_middle
        elif position == "senior":
            salary = self.salary_middle
        else:
            salary = self.salary_min

        if qauntity_projects > 2:
            bonus += salary*0.3
        return bonus

technical1 = Technical()
print(technical1.bonus_counter('junior',4))
print(technical1.salary_counter(15,500))
print(technical1.days_of_vacation_counter(1,1))

recruter1 = Recruter()
print(recruter1.bonus_counter('middle',12))
print(recruter1.salary_counter(25,1000))
print(recruter1.days_of_vacation_counter(1,0))

technical2 = Technical()
print(technical2.bonus_counter('junior',3))
print(technical2.salary_counter(10,''))