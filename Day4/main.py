lines = open("day4/assignments.txt","r").readlines()
count = 0

#Part 1:
for pair in lines:
	pair = pair.replace("\n","")
	elf1, elf2 = pair.split(",")

	elf1min,elf1max = [int(r) for r in elf1.split("-")]
	elf2min,elf2max = [int(r) for r in elf2.split("-")]

	if (elf1min >= elf2min and elf1max <= elf2max) or (elf2min >= elf1min and elf2max <= elf1max):
		count += 1
	
print(count)

count = 0
for pair in lines:
	pair = pair.replace("\n","")
	elf1, elf2 = pair.split(",")

	elf1min,elf1max = [int(r) for r in elf1.split("-")]
	elf2min,elf2max = [int(r) for r in elf2.split("-")]

	if elf2max >= elf1min >= elf2min or elf1max >= elf2min >= elf1min:#got help with this formula
		count += 1



print(count)
