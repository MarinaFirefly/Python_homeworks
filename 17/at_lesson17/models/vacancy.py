class Vacancy:
    #in **data any additional information can be put
    def __init__(self,title,main_skill,main_skills_level,**data):
        self.title = title
        self.main_skill = main_skill
        self.main_skills_level = main_skills_level
        self.data = data