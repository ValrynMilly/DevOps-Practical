####### DEVOPS PRACTICAL PROJECT #######

# The project will start as a single
# Python file where all services work
# as functions. Service one will manage
# communication, service two will manage
# the name generation service three will
# manage title generation and finally
# service four will create a short user
# story based on service 2 & 3.

import random
import sys

####### FUNCTION TWO - NAME GENERATOR
def namegen(input):
    global username
    names = input.split(" ") ##This is going to be a get request
    orcnames = ['uk', 'guk', 'keg', 'rag', 'kha', 'rok', 'zok', 'huk', 'rik']
    elvnames = ['iros', 'ilir', 'tris', 'aren', 'ana', 'ina', 'enys', 'ona', 'dir']
    
    if not (len(names) > 1):
        print("Please input your full and last name.")
        print("\n")
        print("Please try again")
        namegen('Emiljano Kurbiba')
        
    first_Name = names[0][:2]
    three_letters_surname = names[-1][:3]
    username = (random.choice(elvnames) + first_Name + three_letters_surname + random.choice(elvnames)) 
    #Currently im feeding a list into a choice but I want the user to be able to choose.
    #Perhaps seperate routes that can be called from home route & html. 
    print(username.upper())

namegen('Emiljano Kurbiba')

####### FUNCTION THREE - TITLE GENERATOR
def titlegen():
    global title
    articles = ['The', 'A']
    descriptive = ['Powerful', 'Dominant', 'Almighty', 'Omnipotent', 'Omniscient', 'Omnibenevolent', 'Ruling', 'Formidable', 'Divine' ,'Hero']
    objective = ['One', 'Demi-God', 'Giant', 'Berzerker', 'Hunter', 'Wizard', 'Born', 'God']

    title = (random.choice(articles) + " " + random.choice(descriptive) + " " + random.choice(objective)) 

    print(title.upper())

titlegen()

print('\n')

####### FUNCTION FOUR - SHORT STORY GENERATOR INCLUDING TWO AND THREE

def storygen():
    where = ['In a bar','On a field', 'Through the clouds', 'Under a mountain', 'Underwater', 'In a town']
    action = ['killed', 'annihilated', 'destroyed', 'Poisoned', 'Petrified', 'Saved', 'Rescued', 'Healed', 'Silenced']
    instrument = ['a pinkie', 'a pencil', 'a hammer', 'a bow', 'lightning', 'fire', 'a hunt']

    shortstory = (random.choice(where) + " " + username + " " + title +" Once " + random.choice(action)+ " " + str(random.randint(1, 3000)) + " MEN WITH " + random.choice(instrument)) 
## This function is utalising globally accessible variables from other function/services which will inevitably be handled through requests
    print(shortstory.upper())

storygen()