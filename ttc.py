#wpp that makes times table

print('Welcome to times table maker!')

print('=======================================================')

number = float(input('Specify your number: '))

mulNumLimit = int(input('Specify the number of length of the table you want your table to be: '))

tableType = int(input('How you want your table to look? [1 = Simple, 2 = Normal]: '))

print('=======================================================')

mulNum = 1
while(mulNum <= mulNumLimit):
    if(tableType == 1):
        print(number * mulNum)
    else:
        print(number, 'x', mulNum, '=', number * mulNum)
    mulNum = mulNum + 1


print('Done!')

print('=======================================================')

rateinput = int(input('Rate me! [1 - 5]: '))

if(rateinput == 1):
    print('What went wrong?')
elif(rateinput == 2):
    print('Why tho?')
elif(rateinput == 3):
    print('Ok.')
elif(rateinput == 4):
    print('Thx :D')
else:
    print('Wow you are great!')

print('=======================================================')

input('Press ENTER to exit')
                



