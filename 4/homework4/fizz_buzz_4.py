#to use this script 3 filenemas must be entered 0 - name of this file 1 - name of file where values for fizz_buzz are 2 - name of file where new values must be put

import sys

filename = sys.argv[1]
f = open(filename, 'r')
new_list = []
for line in f:
	fizz = int(line.split()[0])
	buzz = int(line.split()[1])
	go_to = int(line.split()[2])
	for i in range(1,go_to+1):
		if i%fizz == 0 and i%buzz == 0: new_list.append("FB ")
		elif i%fizz == 0: new_list.append("F ")
		elif i%buzz == 0: new_list.append("B ")
		else: new_list.append(str(i)+" ")
	new_list.append("\n")
print (("").join(new_list))
f.close()

filename = sys.argv[2]
f = open(filename, 'w')
f.write(("").join(new_list))
f.close() 