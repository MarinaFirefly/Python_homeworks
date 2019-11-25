import random
def rand_mark_list():
	return [random.randint(1,5) for element in range(5)]

st_list = ["Ivanov","Petrov","Vasiliev","Timurov","Durov"]
students_dict = {st:rand_mark_list() for st in st_list}

st_aver = {st:sum(students_dict[st])/len(students_dict[st]) for st in students_dict}

sort_list = sorted(st_aver.items(), key=lambda kv: kv[1])

print("The worst student is " + str(sort_list[0][0]) + " with average mark " + str(sort_list[0][1]) + "!")
print("The best student is " + str(sort_list[-1][0]) + " with average mark " + str(sort_list[-1][1]) + "!")