#from .employee import Employee

class Candidate:
    #in **data any additional information can be put
    def __init__(self,full_name,email,technologies,main_skill,main_skills_grade,**data):
        self.full_name = full_name
        self.email = email
        self.technologies = technologies
        self.main_skill = main_skill
        self.main_skills_grade = main_skills_grade
        self.data = data
