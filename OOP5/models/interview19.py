import datetime


class Interview:
    def __init__(self,vacancy,programmer,recruiter,candidate,dt,feedback,result):
        self.vacancy = vacancy
        self.programmer = programmer
        self.recruiter = recruiter
        self.candidate = candidate
        self.dt = dt
        self.feedback = feedback
        self.result = result
    
    @classmethod
    def next_day(cls,obj):
        #method that will add interview to next day
        vac = obj.vacancy
        prog = obj.programmer
        recr = obj.recruiter
        cand = obj.candidate
        real_dt = datetime.datetime.strptime(obj.dt,"%Y-%m-%d")
        dt = datetime.datetime(real_dt.year, real_dt.month, real_dt.day + 1).strftime("%Y-%m-%d")
        return cls(vac,prog,recr,cand,dt,"","")


#testing 
new_int = Interview("C#","Ivanov","Zhorov","Alex","2020-01-12","","")
print(new_int.dt)
next_day_int = Interview.next_day(new_int)
print(next_day_int.dt)
