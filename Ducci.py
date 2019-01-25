# https://www.reddit.com/r/dailyprogrammer/comments/8sjcl0/20180620_challenge_364_intermediate_the_ducci/

# global list
lines = []

def reading_lines(f):
	for line in f:
		lines.append(line.strip('\n'))

	return lines

def writing_to_file(w):
	pass

def function():
	pass

# get absolute difference of current value and the one next to it!
def gettting_absolute_diff():
	pass

# main program -
# getting input from file
with open('sequences.txt', 'r') as f:

	# calling and printing method that read files line by line
	print(reading_lines(f))

with open('sequences.txt', 'w') as fw:
	pass