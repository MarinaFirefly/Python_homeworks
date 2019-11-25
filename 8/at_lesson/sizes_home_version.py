# tuple of sizes, dictinaries are elements of a tuple.
sizes = (
		{'international':'S','ru':'40','eu':'34','fr':'38','it':'38','gb':'8','usa':'6'},
		{'international':'M','ru':'42','eu':'36','fr':'38','it':'40','gb':'10','usa':'8'},
		{'international':'M','ru':'44','eu':'38','fr':'40','it':'42','gb':'12','usa':'10'},
		{'international':'L','ru':'46','eu':'40','fr':'42','it':'44','gb':'14','usa':'12'},
		{'international':'L','ru':'48','eu':'42','fr':'44','it':'46','gb':'16','usa':'14'},
		{'international':'XL','ru':'50','eu':'44','fr':'46','it':'48','gb':'18','usa':'16'},
		{'international':'XL','ru':'52','eu':'46','fr':'48','it':'50','gb':'20','usa':'18'},
		{'international':'XXL','ru':'54','eu':'48','fr':'50','it':'52','gb':'22','usa':'20'},
		)

#get inputs from user
size_type = input("Types of systems: international, ru, eu, fr, it, gb, usa.\nEnter type of system: ")
size = input("Enter size: ")
to_type = input("What type of system want to get? ")

#function for finding sizes
def find_sizes(size_type_f,size_f,to_type_f):
	res = "Your size is "
	cnt = 0
	for element in sizes: 		# look at all elements in tuple
		for key, value in element.items(): 	# look at all elements in dictionary by key and value
			if key == size_type_f and value == size_f: 	# find when size type and size are the same with input data
				res+=element.get(to_type,'undefined. System or size are out of base!') + " " # add value of new type
				cnt+=1
	
	return res + "undefined. System or size are out of base!" if cnt ==0 else res		# return result

print(find_sizes(size_type,size,to_type))