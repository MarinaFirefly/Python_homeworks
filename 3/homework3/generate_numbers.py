# generaates some amount of random numbers
mini_entered = int(input("What value should be minimal? "))
maxi_entered = int(input("What value should be maximum? "))
num_str_entered = int(input("How many string do you whant to get? "))

#generate line with random numbers
import random
def num_rand_to_line(min_num,max_num,amount = 3):
	line = ""
	i = 0
	while i < amount:
		line+=str(random.randint(min_num,max_num)) + " "
		i += 1
	print(line)
	return line

#write line to file
import sys
filename = sys.argv[1]
f = open(filename, 'w') 
for _ in range(0,num_str_entered):
	f.write(num_rand_to_line(mini_entered,maxi_entered)+"\n")
f.close() 
