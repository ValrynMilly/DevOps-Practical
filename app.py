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
def namegen():
    names = input("Please enter your name: ").split(" ") ##This is going to be a get request
    orcnames = ['uk', 'guk', 'keg', 'rag', 'kha', 'rok', 'zok', 'huk', 'rik']
    elvnames = ['iros', 'ilir', 'tris', 'aren', 'ana', 'ina', 'enys', 'ona', 'dir']
    
    if not (len(names) > 1):
        print("Please input your full and last name.")
        print("\n")
        print("Please try again")
        namegen()
        
    first_Name = names[0][:2]
    three_letters_surname = names[-1][:3]
    username = (random.choice(elvnames) + first_Name + three_letters_surname + random.choice(elvnames)) 
    #Currently im feeding a list into a choice but I want the user to be able to choose.
    #Perhaps seperate routes that can be called from home route & html. 
    print(username.upper())

namegen()

####### FUNCTION THREE - TITLE GENERATOR
def titlegen():
    articles = ['The', 'A']
    descriptive = ['Powerful', 'Dominant', 'Almighty', 'Omnipotent', 'Omniscient', 'Omnibenevolent', 'Ruling', 'Formidable', 'Divine' ,'Hero']
    objective = ['One', 'Demi-God', 'Giant', 'Berzerker', 'Hunter', 'Wizard', 'Born', 'God']

    title = (random.choice(articles) + " " + random.choice(descriptive) + " " + random.choice(objective)) 

    print(title.upper())

titlegen()