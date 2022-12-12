lines = open("day3/rucksacks.txt","r").readlines()

#Part 1:
from string import ascii_uppercase, ascii_lowercase
count = 0

for rucksack in lines:
	half = len(rucksack)//2

	comp1 = rucksack[:half]
	comp2 = rucksack[half:]
	counted = []
	
	for l in comp1:
		if l in comp2 and not l in counted:
			if l.islower():
				count += ascii_lowercase.index(l) + 1
			else:
				count += ascii_uppercase.index(l) + 27
			
			counted.append(l)

print("Total priorities of the item types:",count)

#Part 2:
count = 0

for i in range(0,len(lines),3):
	a = lines[i].replace("\n","")
	b = lines[i+1].replace("\n","")
	c = lines[i+2].replace("\n","")


	for l in a:
		if l in b and l in c:
			if l.islower():
				count += ascii_lowercase.index(l) + 1
			else:
				count += ascii_uppercase.index(l) + 27
			break

print("Total priorities of the badges:",count)
