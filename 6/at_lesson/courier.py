# courier should find porch and floor 
flat_num = int(input("Enter the flat number! "))
floors_num = int(input("How many floors in the building? "))
flats_per_floor = int(input("How many flats per floor in the building? "))

#ugly method that uses 2 cycles.
def find_floor_porch(flat,floors,fl_per_floor):
	current_floor = 1
	current_porch = 1
	#looks for porch
	while flat > floors*fl_per_floor:
		flat -= floors*fl_per_floor
		current_porch+=1
	#looks for floor
	while current_floor < floors:
		if flat <= current_floor * fl_per_floor:
			break 
		current_floor+=1
	#returns result
	return print ("Floor {floor} porch {porch}, appartment found!".format(floor = current_floor, porch = current_porch))

find_floor_porch(flat_num,floors_num,flats_per_floor)