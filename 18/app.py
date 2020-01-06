from models.inherited_classes import Programmer
from models.inherited_classes import Recruiter
from models.inherited_classes import Candidate
from models.vacancy import Vacancy

if __name__ == '__main__':
    recurter_vasya = Recruiter("Vasya","Vasov","vasiliy@gmail.com","23-23-234","12-12-12",200)
    print(recurter_vasya.first_name)
    recurter_vasya.save_email_to_file()

    programmer_Ivan = Programmer("Ivan","Ivanov","ivan@gmail.com","12-12-12-1","02-10-12",50,"Java",tech_stack="[C++,Java,C#]",closed_this_month=2)
    programmer_Ivan2 = Programmer("Ivan","Neivanov","ivan2@gmail.com","12-12-12-2","01-01-19",60,"C#",tech_stack="[C++,Java,C#,SQL]",closed_this_month=5)
    programmer_Ivan3 = Programmer("Ivan","Neivanov","ivan@gmail.com","12-12-12-2","01-01-19",70,"C#",tech_stack="[C++,Java,C#,SQL]",closed_this_month=7)
    print(programmer_Ivan.hired_at)
    print(programmer_Ivan2.salary_per_day)
    programmer_Ivan.validate()
    programmer_Ivan2.validate()
    programmer_Ivan3.validate()

    

'''
    candidate_1 = Candidate("Ivan Ivanov","van_ka@gmail.com","[C#,C++]","[C++]","middle")
    candidate_2 = Candidate("Petr Petrov","pet_ka@gmail.com","[Java,C++]","[Java]","middle")
    candidate_3 = Candidate("Zhora Zhorov","zhor_ka@gmail.com","[PHP,JS]","[PHP]","middle")
    candidate_4 = Candidate("Zhora Zhorov","zhor_ka@gmail.com","[PHP,JS]","[PHP]","middle")
    print(candidate_1.full_name)
    print(candidate_2.email)
    print(candidate_3.main_skill)

    def check_emails3(persons):
        emails = []
        for i in persons:
            emails.append(i.email)
        if len(emails) > len(set(emails)):
            raise ValueError

    check_emails3([candidate_1,candidate_2,candidate_3,candidate_4])
'''
"""
    def check_emails(*email):
        print("Some email isn't unique!") if len(set(email)) < len(list(email)) else print("Emails are unique")
    check_emails(candidate_1.email,candidate_2.email,candidate_3.email)
    
    def check_emails2(*email):
        return len(set(email)) == len(list(email))

    if not check_emails2(candidate_1.email,candidate_2.email,candidate_3.email,candidate_4.email):
        raise ValueError
    vacancy_php = Vacancy("PHP","PHP","junior")
    vacancy_Cplus = Vacancy("C++","C++","midle")
    print(vacancy_Cplus.title)
    print(vacancy_php.main_skill)
"""
