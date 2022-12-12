lines = open("calorieInput.txt","r").readlines()

#Part 1:
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

#Part 2:
this_elf_total = 0 #total of calories for this elf
total_elves = 1 #count of all elves

first_elf = 0 #total of first elf
second_elf = 0 #total of 2nd elf
third_elf = 0 #total of 3rd elf

for line in lines:
	if line == "\n":#this is a gap separating elf
		if this_elf_total > first_elf:
			third_elf = second_elf
			second_elf = first_elf
			first_elf = this_elf_total

		elif this_elf_total > second_elf:
			third_elf = second_elf
			second_elf = this_elf_total

		elif this_elf_total > third_elf:
			third_elf = this_elf_total
		
		
		this_elf_total = 0
		total_elves += 1
	else:
		this_elf_total += int(line.replace("\n",""))


print(f"There were {total_elves} elves. Calorie Leaderboards:\n🥇1st: {first_elf}\n🥈2nd: {second_elf}\n🥉3rd: {third_elf}\n\nThe total is: {first_elf+second_elf+third_elf}")
