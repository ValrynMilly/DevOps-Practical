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

####### FUNCTION FOUR - SHORT STORY GENERATOR INCLUDING TWO AND THREE

def storygen():
    where = ['In a bar','On a field', 'Through the clouds', 'Under a mountain', 'Underwater', 'In a town']
    action = ['killed', 'annihilated', 'destroyed', 'Poisoned', 'Petrified', 'Saved', 'Rescued', 'Healed', 'Silenced']
    instrument = ['a pinkie', 'a pencil', 'a hammer', 'a bow', 'lightning', 'fire', 'a hunt']

    shortstory = (random.choice(where) + " " + username + " " + title +" Once " + random.choice(action)+ " " + str(random.randint(1, 3000)) + " MEN WITH " + random.choice(instrument)) 
## This function is utalising globally accessible variables from other functions which will inevitably be handled through requests
    print(shortstory.upper())

storygen()