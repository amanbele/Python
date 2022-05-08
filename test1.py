words = 'Hi this is typewriting experience'

from time import sleep


scenePlane = [['It is evening 6 pm, Just a normal flight.'], ['''*some screeching noises*''']
                          , ['Wait.. '], ['[Announcement] :> Some fatal issues have occured'], ['Oh No!']
                        , ['We have lost one of our engines!']]

print('Starting the game...')
print('(Press ENTER to continue after each dialogue)')


for char in  scenePlane[1]:
    sleep(0.05)
    print(char, end='', flush=True)
