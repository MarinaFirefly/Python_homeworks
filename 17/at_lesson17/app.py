from models.programmer import Programmer
from models.recruiter import Recruiter
from models.candidate import Candidate
from models.vacancy import Vacancy

if __name__ == '__main__':
    recurter_vasya = Recruiter("Vasya","vasiliy@gmail.com","23-23-234",200)
    print(recurter_vasya)
    print(recurter_vasya.work())
    print(recurter_vasya.check_salary())

    programmer_Ivan = Programmer("Ivan","ivan@gmail.com","12-12-12-1",50,tech_stack="[C++,Java,C#]",closed_this_month=2)
    programmer_Ivan2 = Programmer("Ivan","ivan2@gmail.com","12-12-12-2",60,tech_stack="[C++,Java,C#,SQL]",closed_this_month=5)
    if programmer_Ivan > programmer_Ivan2:
        print ("More skills")
    else: print ("Not more skills!")

    candidate_1 = Candidate("Ivan Ivanov","van_ka@gmail.com","[C#,C++]","[C++]","middle")
    candidate_2 = Candidate("Petr Petrov","pet_ka@gmail.com","[Java,C++]","[Java]","middle")
    candidate_3 = Candidate("Zhora Zhorov","zhor_ka@gmail.com","[PHP,JS]","[PHP]","middle")
    print(candidate_1.full_name)
    print(candidate_2.email)
    print(candidate_3.main_skill)

    vacancy_php = Vacancy("PHP","PHP","junior")
    vacancy_Cplus = Vacancy("C++","C++","midle")
    print(vacancy_Cplus.title)
    print(vacancy_php.main_skill)
