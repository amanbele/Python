import secrets
import string
print('Welcome to Discord Nitro Generator')
print('This is an official nitro generator used by discord itself!')

userInput = int(input('Input amount of codes you want to generate: '))

import random
import string

s = string.ascii_letters + string.digits



for x in range(0,userInput):
    print('[GENERATOR]', "http://discord.gift/" +  (''.join(random.choice(s) for i in range(16))))
    
input("Press ENTER to exit")



