# courier should find porch and floor 
flat_num = int(input("Enter the flat number! "))
floors_num = int(input("How many floors in the building? "))
flats_per_floor = int(input("How many flats per floor in the building? "))

def find_floor_porch(flat,floors,fl_per_floor):
	current_floor = 1
	current_porch = 1
	while flat > floors*fl_per_floor:
		flat -= floors*fl_per_floor
		print(flat)
		current_porch+=1
		print (current_porch)
	while current_floor < floors:
		if flat <= current_floor * fl_per_floor:
			break 
		current_floor+=1
	return ("Floor {floor} porch {porch}, appartment found!".format(floor = current_floor, porch = current_porch))

print(find_floor_porch(flat_num,floors_num,flats_per_floor))
