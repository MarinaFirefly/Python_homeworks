#gets dividers of the number
print ("Enter number...")
x = int(input())
for i in range(1,x+1):
	if x%i== 0:
		print (i)