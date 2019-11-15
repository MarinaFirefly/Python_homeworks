#to use this script 3 filenemas must be entered 0 - name of this file 1 - name of file where values for fizz_buzz are 2 - name of file where new values must be put

import sys

filename = sys.argv[1]
f = open(filename, 'r')

def fizz_buzz(i):
	res = ""
	if int(i)%fizz == 0 and int(i)%buzz == 0: res += "FB"
	elif int(i)%fizz == 0: res += "F"
	elif int(i)%buzz == 0: res += "B"
	else:  res += str(i)
	return res

for line in f:
	new_list = []
	[new_list.append(i) for i in range(1,int(line.split()[2])+1)]
	fizz = int(line.split()[0])
	buzz = int(line.split()[1])		
	result = list(map(fizz_buzz,new_list))
	print((' ').join(result))

filename = sys.argv[2]
f = open(filename, 'w')
f.write((' ').join(result))
f.close() 