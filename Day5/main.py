lines = open("day5/instructions.txt","r").readlines()

#Part 1:
#get starting stacks
stacks = [
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[]
]

#loop thru lines, counting columns and filling stack lists
for i in range(0,8):
	line = lines[i]
	line = line.replace("[","").replace("]","").replace("    "," .").replace(" ","")

	stack = 0
	for l in line:
		if l != "." and l != "\n":
			stacks[stack].insert(0,l)

		stack += 1

#reverse the stacks
count = 0
for stack in stacks:
	stacks[count] = [*reversed(stack)]
	count += 1

#do the moving
for i in range(10,len(lines)):
	line = lines[i].replace("move", "").replace("from", "").replace("to", "").replace("  ", " ").replace("\n","")
	_,amt,mfrom,to = line.split(" ")
	amt = int(amt)
	mfrom = int(mfrom) - 1
	to = int(to) - 1

	for i in range(amt):
		top = stacks[mfrom][0]
		stacks[mfrom].pop(0)

		stacks[to].insert(0,top)

code = ""

for stack in stacks:
	code += stack[0]

print("The final code is:", code)
print("(Stacks were):", stacks)

stacks = [
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[],
	[]
]

#get stacks again
#loop thru lines, counting columns and filling stack lists
for i in range(0,8):
	line = lines[i]
	line = line.replace("[","").replace("]","").replace("    "," .").replace(" ","")

	stack = 0
	for l in line:
		if l != "." and l != "\n":
			stacks[stack].insert(0,l)

		stack += 1

#reverse the stacks
count = 0
for stack in stacks:
	stacks[count] = [*reversed(stack)]
	count += 1


#do the moving
for i in range(10,len(lines)):
	line = lines[i].replace("move", "").replace("from", "").replace("to", "").replace("  ", " ").replace("\n","")
	_,amt,mfrom,to = line.split(" ")
	amt = int(amt)#-1?
	mfrom = int(mfrom) - 1
	to = int(to) - 1

	tomove = stacks[mfrom][:amt]

	for crate in reversed(tomove):
		stacks[mfrom].pop(0)
		stacks[to].insert(0,crate)

code = ""

for stack in stacks:
	code += stack[0]

print("The final code is:", code)
print("(Stacks were):", stacks)
