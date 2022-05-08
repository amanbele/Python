#Decision Game
from time import sleep


#variables Default = 100
health_player = 100
strength_player = 100
hunger_player = 100
mood_player = 100
bal_player = 10

#inventory of player (4 slots)
inv_player = ['Air', 'Air', 'Air', 'Air']

#gameplay
#start

welcome = '''Welcome to the desision game!
This game is totally fitional and not contains any references to real life in any way.'''

for welChar in welcome:
    sleep(0.1)
    print(welChar, end='', flush=True)

print()
proceed_player = str(input('Are you ready to proceed? Y or N: '))

if (proceed_player == 'Y'):
    print('Okay! Have fun and stay safe :D')
else:
    print('Welp, bye -_-')
    quit()

#gameplay
#plane scene
scenePlane = [['It is evening 6 pm, Just a normal flight.'], ['''*some screeching noises*''']
                          , ['Wait.. '], ['[!] :> Some fatal issues have occured'], ['Oh No!']
                        , ['We have lost one of our engines!']]

print('Starting the game...')
print('(Press ENTER to continue after each dialogue)')
print(scenePlane[0])
input()
print(scenePlane[1])
input()
print(scenePlane[2])
input()
print(scenePlane[3])
input()
print(scenePlane[4])
input()
print(scenePlane[5])





