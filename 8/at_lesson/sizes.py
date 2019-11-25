import sys		#to work with files
import json

f = open('sizes.txt', 'r')
sizes = json.loads(('').join(line for line in f))
f.close()

size_type = str(input("Enter type of system (ru/international): "))
size = str(input("Enter size: "))
to_type = str(input("What type of system want to get?"))

print (sizes[size_type][size][to_type])