#wpp 8ball

userinput = input("What's the question? ")

import random

rint = random.randint(1, 20)

if(rint == 1):
    print('> It is certain.')
elif(rint == 2):
    print('> You have got no choice')
elif(rint == 3):
    print('> Ahh, Umm can you explain it to me again?')
elif(rint == 4):
    print('> Nevermind')
elif(rint == 5):
    print('> I need to think about this')
elif(rint == 6):
    print("> I'd say yes!")
elif(rint == 7):
    print('> NO')
elif(rint == 8):
    print('> Welp, you have to do it anyways right?')



