import sys		#to work with files
import json

f = open('sizes.txt', 'r')
sizes = json.loads(('').join(line for line in f))
f.close()

size_type = str(input("Enter type of system (ru/international): "))
size = str(input("Enter size: "))
to_type = str(input("What type of system want to get?"))

# def find_sizes(size_type_f,size_f,to_type_f):
# 	return sizes[size_type_f][size_f][to_type_f]

# print(find_sizes(size_type,size,to_type))
# print (sizes["usa"][str(10)]['international'])

print (sizes[size_type][size][to_type])
# print (size_type,size,to_type)