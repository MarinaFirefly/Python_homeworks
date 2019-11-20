#function find_max_dif finds the maximal difference between elements of 2 lists and returns its length and which elements have the maximal difference.
#list should have same length. In other way function zip will take the shortest list as a basis 

list1 = [12,34,565,345345]
list2 = [123123,67,78,12444]

str1 = "Is this the real life?"
str2 = "Is this just fantazy?"
list3 = str1.split(" ")
list4 = str2.split(" ")

new_list = []

def find_max_dif(i,j):
	#check that both arguments are lists. Otherwise functions returns message "At least one of the arguments isn't list!"
	#add differences in length of elements to new_list. Values in the list is always positive because abs() is used
	new_list.append(abs(len(str(i)) - len(str(j))))
	return new_list

def main_func(l1,l2):
	new_list = []
	ugly_list = list(map(find_max_dif,list1,list2))
	return print("Maximal difference in length is " + str(max(ugly_list[0])) + " between " + str(ugly_list[0].index((max(ugly_list[0])))) + " elements!")

main_func(list1,list2)
# map(find_max_dif,list3,list4)
# map(find_max_dif,"sad",list4)