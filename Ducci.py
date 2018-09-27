# https://www.reddit.com/r/dailyprogrammer/comments/8sjcl0/20180620_challenge_364_intermediate_the_ducci/
# https://github.com/perryc85/ducci_sequence.git

def converting_data_into_lists(numbers):
	# creating list
	numbers = numbers.split(',')

	# removing unwanted indicies cointaining strings - no mixing data here!
	numbers.pop(0)
	numbers.pop(-1)

	return numbers

def function(numbers):
	pass

# get absolute difference of current value and the one next to it!
def gettting_absolute_diff():
	pass

# main program -
# getting input from file
with open('sequences.txt', 'r') as f:

	# iterate over the entire file turning the data into ints
	for numbers in f:
		print(converting_data_into_lists(numbers))



		# int_numbers = int(numbers)
		# print(numbers)
