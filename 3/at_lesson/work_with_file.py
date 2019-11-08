"""
import sys
filename = sys.argv[1]
# далее открываем файл на чтение (опция 'r')
f = open(filename, 'r') # в файле теперь file descriptor
for line in f: # для каждой строки в файле
	print(line)
f.close() # закрытие файла
"""
import sys
filename = sys.argv[1]
f = open(filename, 'r') 
for line in f:
	li = [int(x) for x in line.split()] # list complication
	print(li)
"""	print(line)
	li = line.split()
	print(li)
	li = list(map(int,li))
	print(li)
"""
f.close()