#gets students and their marks also shows average mark
#get() is more preferable than array[i] because it not causes errors and just return 'None' or default value
#get(stud_dict.get(student,'Vasya')) default student Vasya

import random

students = ['Misha','Eugen','Toma','Gora','Marusya']

stud_dict = {}
for student in students:
	stud_dict[student] = []
	for _ in range(1,6): # "_" doesn't make a new variable and will work faster
		stud_dict[student].append(random.randint(1,5))
print(stud_dict)

for student in stud_dict:
	#print(sum(stud_dict[student])/len(stud_dict[student]))
	#print(sum(stud_dict.get(student))/len(stud_dict.get(student)))
	print("Student {name} has average mark {mark}"\
		.format (
			name = student,
			mark = sum(stud_dict.get(student))/len(stud_dict.get(student))))

