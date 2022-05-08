#wwp for calculating gross salary of a specific person.

#values
#values to be entered below

personName = 'Ramesh'

dValue = 100                    #value used for calculating percentages

basicSalary = 15000             #value for specifying person's basic salary

sAllowence = 40                 #allowed value by person2

houseRent = 20                  #house rent percentage

#calculations

calcAllowence = basicSalary / dValue * sAllowence

calcRent = basicSalary / dValue * houseRent

#final calculation

grossSalary = basicSalary + calcAllowence + calcRent

#print final result

print('########################')
print('Gross Salary Calculation')
print()
print('Person       :', personName)
print('Salary       :', basicSalary)
print('Allowed Value:', sAllowence)
print('House Rent   :', houseRent)
print()
print('Gross Salary :', grossSalary)
print('########################')

