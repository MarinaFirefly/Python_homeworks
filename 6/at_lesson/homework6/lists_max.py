#function find_max_dif finds the maximal difference between elements of 2 lists and returns its length and which elements have the maximal difference.
#list should have same length. In other way function zip will take the shortest list as a basis 

list1 = [12,34,565]
list2 = [123123,67,78,12444]

str1 = "Is this the real life?"
str2 = "Is this just fantazy?"
list3 = str1.split(" ")
list4 = str2.split(" ")

#function find_max_dif takes 2 lists as parameters
def find_max_dif(l1,l2):
	#check that both arguments are lists. Otherwise functions returns message "At least one of the arguments isn't list!"
	if type(l1) != list or type(l2) != list:
		return (print("At least one of the arguments isn't list!"))
	else:	
		new_list = []
		for i, j in zip(l1,l2):
			#add differences in length of elements to new_list. Values in the list is always positive because abs() is used
			new_list.append(abs(len(str(i)) - len(str(j))))
		#return string containing maximal value from new_list and its possition in the list starting from 0
		return print("Maximal difference in length is " + str(max(new_list)) + " between " + str(new_list.index((max(new_list)))) + " elements!")

find_max_dif(list1,list2)
find_max_dif(list3,list4)
find_max_dif("sad",list4)