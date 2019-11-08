fizz = int(input("fizz = "))
buzz = int(input("buzz = "))
go_to = int(input("last number = "))
i = 1
while i < (go_to+1):
	if i%fizz == 0 and i%buzz == 0:
		print("FB")
	elif i%fizz == 0:
		print("F")
	elif i%buzz == 0:
		print("B")
	else:
		print (i)
	i+=1