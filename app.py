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
import string

####### FUNCTION THREE - TITLE GENERATOR
def titlegen():
    articles = ['The', 'A']
    descriptive = ['Powerful', 'Dominant', 'Almighty', 'Omnipotent', 'Omniscient', 'Omnibenevolent', 'Ruling', 'Formidable', 'Divine' ,'Hero']
    objective = ['One', 'Demi-God', 'Giant', 'Berzerker', 'Hunter', 'Wizard', 'Born', 'God']

    title = (random.choice(articles) + " " + random.choice(descriptive) + " " + random.choice(objective)) 

    print(title.upper())

titlegen()