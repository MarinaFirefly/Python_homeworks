flats_per_floor = 8 
floors = 24

flat_required = int(input())
current_floor = 1
while current_floor < floors+1:
	if flat_required <= current_floor * flats_per_floor:
		print("Floor {cur}, appartment found!".format(cur = current_floor))
		break
	current_floor+=1