def star(number):
    for i in range(number):
        quantity_slash = abs(number // 2 - i)
        print(f"{' ' * quantity_slash}{'*' * (number - quantity_slash * 2)}")
    return

num = int(input("Enter odd number! "))
if num%2 == 1:
	star(num)
else: print ("Number isn't odd!")