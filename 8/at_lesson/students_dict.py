import random

#function creates list of 5 random marks
def rand_mark_list():
	return [random.randint(1,5) for element in range(5)]

# list of students
st_list = ["Ivanov","Petrov","Vasiliev","Timurov","Durov"]
#dictionary with students as keys and list of their random marks as values
students_dict = {st:rand_mark_list() for st in st_list}
#dictionary with students as keys and their average marks as values
st_aver = {st:sum(students_dict[st])/len(students_dict[st]) for st in students_dict}
#return list of students 
sort_list = sorted(st_aver.items(), key=lambda kv: kv[1])

print("The worst student is " + str(sort_list[0][0]) + " with average mark " + str(sort_list[0][1]) + "!")
print("The best student is " + str(sort_list[-1][0]) + " with average mark " + str(sort_list[-1][1]) + "!")