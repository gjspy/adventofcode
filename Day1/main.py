lines = open("calorieInput.txt","r").readlines()

this_elf_total = 0 #total of calories for this elf
total_elves = 1 #count of all elves
highest_cals = 0 #highest elf calories
highest_elf = 0 #id of highest elf

for line in lines:
	if line == "\n":#this is a gap separating elf
		if this_elf_total > highest_cals:
			highest_cals = this_elf_total
		
		this_elf_total = 0
		highest_elf = total_elves
		total_elves += 1
	else:
		this_elf_total += int(line.replace("\n",""))


print(f"There were {total_elves} elves, the elf with the highest calories was Elf #{highest_elf} with {highest_cals} calories!")