import time
import random
from termcolor import colored
import sys


# add diamends by doing random on blank cells
def do_diamonds_on_blank(blank, diamonds): # blank_character | diamonds_character
	 
		diamonds_weight = [0.99, 0.05]
		final_cell = random.choices([blank, diamonds], diamonds_weight)[0]

		return colored(f'{final_cell}', 'yellow')


def display_street(left_street):

	for line in left_street:
		# print(' ', end='', flush=True)
		print()

		for i in line:
			# print(f"{i} .", end='', flush=True)
			sys.stdout.write(f'{i} .')

		sys.stdout.write("\b")
		sys.stdout.write("|")
		time.sleep(0.04)


def step_up_all(left_street):
	def step_this_item_up(item):
		pass
	pass


def create_random_line():
	pass




if __name__ == "__main__":

	diamonds = '◈' # ◈ optional 
	square = '▣' # ▣ 
	circle = '◉' # ◉ 
	blank = ' '

	E1 = 'E'
	E2 = 'E' 

	left_street = [] # holdes each line of the street in horizontal(ofoghi)
	
	blank_circle_square = [blank, circle, square]
	item_weight = [0.99, 0.2, 0.1]

	# square_blocking vars
	save_continuous_sq = []
	give_it_blank_line = 0
	distance_between_sq = 2 # in some situation if randomly two squars become chosen (wich block the street!) how many lines be empty is stored in "distance_between_sq" var


	# choose_diamonds = input("type just y if you want diamonds then whatever you type you wont have diamonds! \ndiamonds(Y/N)? ").lower()
	# choose_diamonds = (True if choose_diamonds=='y' else False)
	choose_diamonds = False 





	for i in range(52): # 52 is number of lines which can fill whole the terminal display

		chosen_item = random.choices(blank_circle_square, item_weight)[0] # choose either blank or score_character as one item list so I put [0] to take the item itself


		'''
		check if squars are not blocking the street.  e.g. :
		if some situation happened like thi; give it one blank line at least
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
		if idnex == 0:
			left_street.append([chosen_colored, blank])
		else : # index is 1
			left_street.append([blank, chosen_colored])



	# print(left_street)
	display_street(left_street)