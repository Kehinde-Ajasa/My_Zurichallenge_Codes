# This code is used to play the rock paper scissors game.
import random
name = input('Enter your name for familiarity just press space to skip: ')
while True:
	Rock = "R"
	Paper = "P"
	Scissors = "S"
	user_input = input('Enter R for Rock, P for Paper and S for Scissors: ').upper()
	RPS_list = ["R", "P", "S"] # Creating a list of options to ensure user input is within the scope
	if user_input in RPS_list:


		def Game_mode(user_choice):
			"""function to create the logic for the game"""
			options = ["R", "P", "S"]
			computer_choice = random.choice(options) # Randomly selecting an item from the options list above

			if computer_choice == Rock and user_choice == Scissors:# conditional statement 1
				return f'CPU wins [{name}({user_choice}): CPU({computer_choice})]'


			elif computer_choice == Paper and user_choice == Rock: # conditional statement 2
				return f'CPU wins [{name}({user_choice}) : CPU({computer_choice})]'


			elif computer_choice == Scissors and user_choice == Paper: # conditional statement 3
				return f'CPU wins [{name}({user_choice}) : CPU({computer_choice})]'

			elif computer_choice == user_choice: # conditional statement 4 and creation of logic for the occurence of a tie
				print(f'TIE!!! [{name}({user_choice}) : CPU({computer_choice})]')
				new_user_input = input("Enter new option R for Rock, P for Paper and S for Scissors: ")
				return Game_mode(new_user_input) # replacing the parameter of the main game_mode function to the new input if there is a tie
			else: # final conditional statement (all in favour of the user)
				return f' {name} wins [{name}({user_choice}): CPU({computer_choice})]'


		print(Game_mode(user_input))
		break
	else:
		print("The option you picked doesnt exists.")