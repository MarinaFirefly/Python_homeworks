# courier should find porch and floor 
flat_num = int(input("Enter the flat number! "))
floors_num = int(input("How many floors in the building? "))
flats_per_floor = int(input("How many flats per floor in the building? "))

def courier(flat,floors,flats_floor):
	flats_porch = flats_floor*floors #finds quantity of flats per porch
	porch = flat_num//flats_porch + 1
	floor = (flat_num%flats_porch)//flats_floor +1
	return ("Floor {floor} porch {porch}, appartment found!".format(floor = floor, porch = porch))

print(courier(flat_num,floors_num,flats_per_floor))