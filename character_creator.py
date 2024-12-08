from beings import *
from races import *


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
    num = 0
    for i in race_list:
        print(f"{num} - " + i['race_name']+ "  - " + i['description'])
        num += 1
    print("Type the n")



#player = Player(race,sex,choose_name(),level,mainjob, subjob, starting_gold,"staff",current_exp, exptnl)


#print(f"Welcome {player.name}, it's good to meet you.")
#print(f"You are a {player.mainjob}/{player.supportjob} at level {player.level}, you have {player.gold} gold and your invetory only has {player.inventory}")

#print(choose_name())male

choose_race()
