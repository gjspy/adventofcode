lines = open("day2/strategyGuide.txt","r").readlines()

#Part 1:
my_score = 0

words = {
	"A":"rock",
	"B":"paper",
	"C":"scissors",

	"X":"rock",
	"Y":"paper",
	"Z":"scissors"
}

#string format: elf_action-my_action
i_win = [
	"rock-paper",
	"paper-scissors",
	"scissors-rock",
]

elf_win = [
	"rock-scissors",
	"paper-rock",
	"scissors-paper"
]

"""
	X rock v rock
	I rock v paper
	E rock v scissors

	E paper v rock
	X paper v paper
	I paper v scissors

	I scissors v rock
	E scissors v paper
	X scissors v scissors
	"""

action_scores = {
	"rock":1,
	"paper":2,
	"scissors":3
}

for line in lines:
	args = line.replace("\n","").split(" ")

	elf_ltr = args[0]
	my_ltr = args[1]

	elf_action = words[elf_ltr]
	my_action = words[my_ltr]
	action_code = elf_action + "-" + my_action

	my_score += action_scores[my_action]#score of selected shape

	if action_code in i_win:#add 6 if win
		my_score += 6

	elif action_code in elf_win:#pass if lost (don't add more)
		pass

	else:#draw, add 3
		my_score += 3


print(f"My total score was: {my_score} (Part 1)")

#Part 2:
words = {
	"A":"rock",
	"B":"paper",
	"C":"scissors",

	"X":"lose",
	"Y":"draw",
	"Z":"win"
}

#how to end based on elf input
how_to_end = {
	"rock":{
		"lose":"C", #scissors
		"draw":"A", #rock
		"win":"B", #paper
	},

	"paper":{
		"lose":"A", #rock
		"draw":"B", #paper
		"win":"C", #scissors
	},

	"scissors":{
		"lose":"B", #paper
		"draw":"C", #scissors
		"win":"A", #rock
	}
}

my_score = 0

for line in lines:
	args = line.replace("\n","").split(" ")


	elf_action = words[args[0]]
	win_status = words[args[1]]

	my_ltr = how_to_end[elf_action][win_status]
	my_action = words[my_ltr]

	action_code = elf_action + "-" + my_action

	my_score += action_scores[my_action]#score of selected shape

	if win_status == "win":#add 6 if win
		my_score += 6

	elif win_status == "lose":#pass if lost (don't add more)
		pass

	else:#draw, add 3
		my_score += 3

print(f"My total score was: {my_score} (Part 2)")
