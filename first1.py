#wpp that makes times table

print('Welcome to times table maker!')

number = int(input('Specify your number: '))

mulNumLimit = int(input('Specify the number of length of the table you want your table to be: '))


mulNum = 1
while(mulNum <= mulNumLimit):
    print(number, 'x', mulNum, '=', number * mulNum)
    mulNum = mulNum + 1

print('Done!')



