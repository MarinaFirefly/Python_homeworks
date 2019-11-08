#to use this script 3 filenemas must be entered 0 - name of this file 1 - name of file where values for fizz_buzz are 2 - name of file where new values must be put

# function fizz_buzz returns line with FB, F, B or number according to conditions
def fizz_buzz(fizz,buzz,go_to):
	i = 1
	line = ""
	while i < (go_to+1):
		if i%fizz == 0 and i%buzz == 0:
			line += "FB "
		elif i%fizz == 0:
			line += "F "
		elif i%buzz == 0:
			line += "B "
		else:
			line += str(i) + " "
		i+=1
	return line

#this part of code reads lines from file and aply fizz_buzz funtion for them
import sys
def change_file():
	filename = sys.argv[1]
	f = open(filename, 'r')
	line_out = ""
	for line in f:
		fizz_read = int(line.split()[0])
		buzz_read = int(line.split()[1])
		go_to_read = int(line.split()[2])
		#print(fizz_buzz(fizz_read,buzz_read,go_to_read))
		line_out += str(fizz_buzz(fizz_read,buzz_read,go_to_read))+"\n"
	return line_out
	f.close()

# this part writes result to new file
filename = sys.argv[2]
f = open(filename, 'w') 
f.write(change_file())
f.close() 