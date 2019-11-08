#gets positive answer if number is odd and can be divided to 3 and 5 and cannot be divivded to 10
print ("Enter number...")
x = int(input())
if x%2 and not x%3 and not x%5 and x%10:
	print ("Yes! That is!")
else:
	print ("Not that number!")
