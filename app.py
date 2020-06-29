import random
import sys

names = input("Please enter your name: ").split(" ")


orcnames = ['uk', 'guk', 'keg', 'rag', 'kha', 'rok', 'rok', 'huk']
elvnames = ['iros', 'ilir', 'tris', 'aren', 'ana', 'ina', 'enys', 'ona', 'dir']


if not (len(names) > 1):
    print("Please input your full and last name.")
    sys.exit()

first_Name = names[0][2]
three_letters_surname = names[-1][:3]
number = '{:03d}'.format(random.randrange(1, 999))
username = (first_Name + three_letters_surname + random.choice(elvnames))
print(username)