#gets number position of number
print ("Enter number to get it's number position...")
x = int(input())
print (x)
power = 0
while x > 0:
	print (x%10,"* 10 ^",power)
	x//=10
	power+=1