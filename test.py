'''import string, random

random_string = ''

for x in range(18):
    if random.choice([1,2]) == 1:
        random_string += random_string.join(random.choice(string.ascii_letters))
    else:
        random_string += random_string.join(random.choice(string.digits))
print(random_string)
'''
userInput = int(input('Input amount of codes you want to generate: '))

import random
import string

s = string.ascii_letters + string.digits

for x in range(0,userInput):
    print(''.join(random.choice(s) for i in range(16)))
