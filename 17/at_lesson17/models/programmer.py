from .employee import Employee


# class Programmer is inherited from Employee
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
    def __add__(self,other):
        return self.day_salary + other.day_salary
