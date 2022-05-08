#try except

userin = int(input("Enter your first number: "))
userin2 = int(input("Enter your second number: "))

print("Statement 1")
try:
    print(userin / userin2)
except ZeroDivisionError:
    print("You tried to divide a number by zero!")
except ValueError:
    print("I accept integer values only!")
except:
    print("Something seems wrong.")

print("Statement 2")

try:
    x = int(input("Enter your first number: "))
    y = int(input("Enter your second number: "))
    print(x/y)
except (ZeroDivisionError, ValueError) as msg:
    print("Oh, You've raised an exception!")
    print("Exception: ",msg.__class__.__name__)
    print("Description of the error: ", msg)
