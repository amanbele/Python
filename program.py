#program to make a calc

import calendar


                      

# display the calendar

inputYear = int(input('What year you want to choose?: '))
inputMonth = int(input('What month you want to choose?: '))

def cal (inputYear, inputMonth):
    
    print('=====================')
    print(calendar.month(inputYear, inputMonth))
    print('=====================')
    

cal(inputYear, inputMonth)

