import time
import os



def step_up(street):
	print(f'-----\n{x}\n-----')
	i = 0
	while True:
		
		i += 1

		if i == len(street)-1:
			street[i] = ['.', '.']
			break

		# i starts from 1 so the first cell which is E is ignored
		street[i] = street[i+1]
		
		

	return street 



if __name__ == '__main__':
	global x
	x = 19
	street = [
		['E', 'E'],
		['A', '.'],
		['.', '.'],
		['.', 'A'],
		['.', '.'],
		['A', '.'],
		['.', 'A'],
		['.', 'A'],
		['A', '.'],
		['.', '.'],
		['.', 'A'],
		['.', '.'],
		['A', '.'],
		['.', 'A'],
		['.', 'A'],
		['A', '.'],
		['.', '.'],
		['.', 'A'],
		['.', '.'],
		['A', '.'],
		['.', 'A'],
		['.', 'A'],
		['A', '.'],
		['.', '.'],
		['.', 'A'],
		['.', '.'],
		['A', '.'],
		['.', 'A'],
		['.', 'A']

	]

	os.system('clear')
	time.sleep(1)

	for i in range(40):

		
		for line in street:
			
			print(' |', end='')
			for cell in line:
				print(f'{cell}|', end='', flush=True)
			print()

		street = step_up(street)

		time.sleep(0.07)
		os.system('cls')
