#An adventure based user-input game in Central Illinois

import random
import sys

game_locations = ['Champaign','Savoy','Urbana','Danville']

game_characters = ['Chancellor Jones','Alma mater','Stressed Undergrad',"Joe's Doorguy"]

story_options = ['Washington Park','Foelinger','Six Pack']

playing = True



def location():

	print(f'Your adventure can take place in {game_locations[0]}, {game_locations[1]}, {game_locations[2]}, or {game_locations[3]}')

	chosen_location = []
	
	ask_location = input("Where do you want to start your journey?\nType 'C' for Champaign\n'S' for Savoy\n'U' for Urbana\n'D' for Danville\nYour choice:")

	if ask_location.lower() == 'c':
		print('You have chosen Champaign for your adventure')
		chosen_location.append('Champaign')
	elif ask_location.lower() == 's':
		print('You have chosen Savoy for your adventure')
		chosen_location.append('Savoy')
	elif ask_location.lower() == 'u':
		print('You have chosen Urbana for your adventure')
		chosen_location.append('Urbana')
	elif ask_location.lower() == 'd':
		print('You have chosen Danville for your adventure')
		chosen_location.append('Danville')
	else:
		print('Sorry, please try again')


def character():

	user_character = []

	print(f'The characters are {game_characters[0]}, {game_characters[1]}, {game_characters[2]}, {game_characters[3]}')
	ask_character = int(input('Choose your character.\nType 0 for Chancellor Jones\n1 for Alma mater\n2 for Stressed Undergrad\n3 for Joes Doorguy: '))

	if ask_character == 0:
		print(f'You have chosen {game_characters[0]}')
		user_character.append([game_characters[0]])
	elif ask_character == 1: 
		print(f'You have chosen {game_characters[1]}')
		user_character.append([game_characters[1]])
	elif ask_character == 2:
		print(f'You have chosen {game_characters[2]}')
		user_character.append([game_characters[2]])
	elif ask_character == 3:
		print(f'You have chosen {game_characters[3]}')
		user_character.append([game_characters[3]])
	else:
		print('Sorry, try again')

def journey():
    
	journey_choice = []


	print(f'You can go down three different pathways in this game\nYou can start at {story_options[0]}, {story_options[1]}, or {story_options[2]}')
	journey_input = int(input(f'Which journey path would you like to try? Type 0 for {story_options[0]}, 1 for {story_options[1]} and 2 for {story_options[2]}: '))

	if journey_input == 0:
		print(f'You have chosen {story_options[0]}')
		journey_choice.append(story_options[0])
	elif journey_input == 1:
		print(f'You have chosen {story_options[1]}')
		journey_choice.append(story_options[1])
	elif journey_input == 2:
		print(f'You have chosen {story_options[2]}')
		journey_choice.append(story_options[2])
	else:
		print('please try again')

	journey_choice_str = str(journey_choice)

	x = int(input(f'Are you ready for the journey?! You are standing at {journey_choice_str} do you: go inside? turn around? 1 for go inside, 2 for turn around'))
	if x == 1:
		print("I'll need to see your safer illinois status first")
		print("It looks like you don't have building access! Go Home!")
	elif x == 2:
		print('Smart choice, you should be socially-distancing')
	else:
		print('try again')

def finish():
	print("The goal of this game was not to go on an advernture\nIn fact, it was the opposite.\nThis game is meant to show you that now is not a good time for adverntures\nIn order to defeat COVID-19, we all have to socially distance!\nI hope you takeaway from this game the fact that we're all in this together, and that we have to stay safe together!")
	print('Thanks for playing, hopefully next update there will be more adventure!')


while playing:

	print("Hello and welcome to the WAM Journey game!\nThis game will only work with your input and enthusiasm.\nYour goal is to finish the journey!\nGood Luck!")
	
	location()

	character()

	journey()

	finish()

	playing = False
	sys.exit()









