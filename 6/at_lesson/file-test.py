#find number of the words in the text and print them as a set
import re		#for regular expressions
import sys		#to work with files

f = open(sys.argv[1],'r')
for line in f:
	line = line.replace('\n','')
	first_part = line.split(';')[0].split(' ')
	second_part = line.split(';')[1].split(' ')
	# first_part = re.findall(r'\d+',str(re.findall(r'.+;',line)))
	# second_part = re.findall(r'\d+',str(re.findall(r';.+',line)))
	cnt = tot = 0
	for i in first_part:
		cnt += 1
		tot += int(i)
	if tot//cnt == int(second_part[0]) and tot%cnt  == int(second_part[1]):
		print(line+"	True")
	elif tot//cnt != int(second_part[0]) and tot%cnt  == int(second_part[1]):
		print(line+"	False" + "	Condition1: " + str(tot//cnt) + " not equal " + second_part[0])
	elif tot//cnt == int(second_part[0]) and tot%cnt  != int(second_part[1]):
		print(line+"	False" + "	Condition2: "+ str(tot%cnt) + " not equal " + second_part[1])
	else:
		print(line+"	False" + "	All conditions are incorrect!")
f.close()