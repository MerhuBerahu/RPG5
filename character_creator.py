from beings import *
from races import *
from utilities import *



# TODO: pulls races from list of available races, create a function to list and select from there


#sex = input("Are you male or female? ")
#race = input("what race are you? ")  # [ ], race list function
level = 1
mainjob = 'whm'
subjob = 'blm'
starting_gold = 10
current_exp = 0
exptnl = 300

def choose_name():
    name = input("Hello adventurer, what is your name? ")
    return name

def choose_race():
    #TODO from races.py list races dict and make a choice
    print("What Race are you?")
    # Display numbered choices
    for index, i in enumerate(race_list, start=1):
        print(f"{index}. {i['race_name']}")
    
    # Get and validate user choice
    selected_index = get_valid_choice(i)
    print(f"Selected Index: {selected_index}")

    selected_choice = race_list[selected_index - 1]
    return selected_choice

def choose_gender():
    gender_choices = ['Male', "Female"]
    print("Which gender are you?")
    # Display numbered choices
    for index, i in enumerate(gender_choices, start=1): # start at 1 instead of index 0, real start
        print(f"{index}. {i}")
    
    # Get and validate user choice
    selected_index = get_valid_choice(gender_choices)
    selected_choice = gender_choices[selected_index - 1] # minus 1 to get actual index position
    return selected_choice
    

player = Player(choose_race(),choose_gender(),choose_name(),1,'whm', 'blm', 10,"staff",100, 300)


#print(f"Welcome {player.name}, it's good to meet you.")
#print(f"You are a {player.sex} {player.race['race_name']}  {player.mainjob}/{player.supportjob} at level {player.level}, you have {player.gold} gold and your invetory only has {player.inventory}")
#print(db.query_table('spells',player.mainjob, player.level))
print_query('spells',player.mainjob, player.level)

