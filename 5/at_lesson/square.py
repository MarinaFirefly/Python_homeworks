#find squres of the simple numbers using map
list_numers = [1,2,3,45,6,8,9,12,8,8,17,29,90,77,113]
#function that calculates squares
def sqrt_num(num):
	return num**2

#function that return new list consisting of simple numbers
def dividers(list_num):
	new_list = []
	for num in list_num:
		i = 2
		cnt = 1 if num == 1 else 0 #take 1 as not simple number
		while i <= num/2:
			if num%i == 0:
				cnt+=1	#if num has dividors between 2 and num/2 cnt is equal 1
				break 	#break if cycle find out some dividor between 2 and num/2
			else: i+=1	
		if cnt == 0: new_list.append(num) 
	return new_list

print(list(map(sqrt_num, dividers(list_numers))))

#ugly method that uses 2 functions: 1 finds dividors and 2 makes a list of simple numbers (besides 1 is simple here)
def div_for_num(num):
	return [i for i in range (1,num) if num%i == 0]
def div_for_list(list_num):
	return [i for i in list_num if len(div_for_num(i))<2]

print(list(map(sqrt_num, div_for_list(list_numers))))