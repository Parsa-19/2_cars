'''
	diamonds = '◈' # ◈ optional 
	square = '▣' # ▣ 
	circle = '◉' # ◉ 
	blank = ' '

'''
import time
import random
from termcolor import colored
import sys
import os

# add diamends by doing random on blank cells
def do_diamonds_on_blank(blank, diamonds): # blank_character | diamonds_character
		diamonds_weight = [0.99, 0.05]
		final_cell = random.choices([blank, diamonds], diamonds_weight)[0]

		return colored(f'{final_cell}', 'yellow')

def print_street(left_street):
	for line in left_street:
		print()
		for i in line:
			sys.stdout.write(f' {i}   ')

		sys.stdout.write("\b")
		sys.stdout.write("|")
	print()

def step_up_all(street):
	i = 0
	while True:
		i += 1
		if i == len(street)-1:
			street[i] = [' ', ' ']
			break
		# i starts from 1 so the first cell which is E is ignored
		street[i] = street[i+1]
		
	return street 

def create_random_line_on_street(diamonds='◈', square='▣', circle='◉', blank=' '):
	global blank_circle_square
	global item_weight
	global save_continuous_sq
	global give_it_blank_line
	global distance_between_sq 
	global choose_diamonds

	chosen_item = random.choices(blank_circle_square, item_weight)[0] # choose either blank or score_character as one item list so I put [0] to take the item itself

	'''
	check if squars are not blocking the street.  e.g. :
	if some situation happened like this; give it two("distance_between_sq") blank line at least
	'''
	if chosen_item == square:
		
		if len(save_continuous_sq) < 2 :
			save_continuous_sq.append(square)

		if len(save_continuous_sq) >= 2:
			chosen_item = blank
			give_it_blank_line += 1
			
			if give_it_blank_line >= distance_between_sq:
				save_continuous_sq = [] # if save_continious_sq become empty; then "chosen" var will be able to be square again
				give_it_blank_line = 0

	if chosen_item == circle:
		chosen_colored = colored(f'{chosen_item}', 'light_blue')
	elif chosen_item == square:
		chosen_colored = colored(f'{chosen_item}', 'red')
	else :
		chosen_colored = chosen_item
	

	if choose_diamonds:
		blank = do_diamonds_on_blank(blank, diamonds)

	idnex = random.choice( [0, 1] )
	random_line = []
	if idnex == 0:
		random_line = [chosen_colored, blank]
	else : # index is 1
		random_line = [blank, chosen_colored]

	return random_line




if __name__ == "__main__":

	diamonds = '◈' # ◈ optional 
	square = '▣' # ▣ 
	circle = '◉' # ◉ 
	blank = ' '

	E1 = 'E'
	E2 = 'E' 

	left_street = [] # holdes each line of the street in horizontal(ofoghi)
	
	global blank_circle_square
	blank_circle_square = [blank, circle, square]

	global item_weight
	item_weight = [0.99, 0.07, 0.04]

	# square_blocking vars
	global save_continuous_sq
	save_continuous_sq = []

	global give_it_blank_line
	give_it_blank_line = 0 # temp var

	global distance_between_sq 
	distance_between_sq = 2 # in some situation if randomly two squars become chosen (wich block the street!) how many lines be empty is stored in "distance_between_sq" var


	# choose_diamonds = input("type just y if you want diamonds then whatever you type you wont have diamonds! \ndiamonds(Y/N)? ").lower()
	# choose_diamonds = (True if choose_diamonds=='y' else False)
	global choose_diamonds
	choose_diamonds = False 

	left_street.append([E1, blank])
	for i in range(51): # 52 is number of lines which can fill whole the terminal display
		random_line = create_random_line_on_street()
		left_street.append(random_line)

	step = 0
	while True:
		os.system('cls')
		step += 1
		
		print(f"step {step}")
		print_street(left_street)
		left_street = step_up_all(left_street)
		random_line = create_random_line_on_street()
		left_street[-1] = random_line

		if step == 600:
			break
			
		time.sleep(0.04)