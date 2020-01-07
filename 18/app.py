import datetime
import traceback
from models.inherited_classes import Programmer
from models.inherited_classes import Recruiter
from models.inherited_classes import Candidate
from models.vacancy import Vacancy

files_with_emails = open('data/emails','w+')
files_with_emails.truncate(0)

try:
    if __name__ == '__main__':
        recurter_vasya = Recruiter("Vasya","Vasov","vasiliy@gmail.com","23-23-234","12-12-12",200)
        print(recurter_vasya.first_name)
        recurter_vasya.save_email_to_file()

        programmer_Ivan = Programmer("Ivan","Ivanov","ivan@gmail.com","12-12-12-1","02-10-12",50,"Java",tech_stack="[C++,Java,C#]",closed_this_month=2)
        programmer_Ivan2 = Programmer("Ivan","Neivanov","ivan2@gmail.com","12-12-12-2","01-01-19",60,"C#",tech_stack="[C++,Java,C#,SQL]",closed_this_month=5)
        programmer_Ivan3 = Programmer("Ivan","Neivanov","ivan3@gmail.com","12-12-12-2","01-01-19",70,"C#",tech_stack="[C++,Java,C#,SQL]",closed_this_month=7)
        print(programmer_Ivan.hired_at)
        print(programmer_Ivan2.salary_per_day)
        print(programmer_Ivan.work())
        programmer_Ivan.validate()
        programmer_Ivan2.validate()
        programmer_Ivan3.validate()

        candidate_1 = Candidate("Ivan","Petrov","van_ka@gmail.com","12-12-123","C++")
        print(candidate_1.work())
        
except ValueError as error:
    with open('data/logs.txt','a+') as f:
        message = '{}   {}:\n {} \n\n'.format(
            datetime.datetime.now(),
            error.__class__.__name__,
            traceback.format_exc()
        )
        f.write(message)
except TypeError as error:
    with open('data/logs.txt','a+') as f:
        message = '{}   {}:\n {} \n\n'.format(
            datetime.datetime.now(),
            error.__class__.__name__,
            traceback.format_exc()
        )
        f.write(message)
else:
    with open('data/logs.txt','a+') as f:
        message = '{}:\n Unknown error'.format(
            datetime.datetime.now()
        )
        f.write(message)
finally:
    print('Exception was handled. Check log for additional info!')
