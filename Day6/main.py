signal = open("day6/signal.txt","r").read()

def get_code(needed_chars):
	code = ""
	num = 0

	for i in range(0,len(signal)):
		if i > needed_chars:
			codetab = [signal[i-a] for a in range(needed_chars-1,-1,-1)]
			codeset = set(codetab)
			#print(len(codetab))

			if len(codetab) == len(codeset):
				code = "".join(codetab)
				num = i + 1
				break
	
	return code,num




#Part 1:
code, num = get_code(4)
print(f"The final packet code was: {code}, which finishes at place {num}.")

#Part 2:
code, num = get_code(14)
print(f"The final message code was: {code}, which finishes at place {num}.")
