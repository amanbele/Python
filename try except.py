#Try and except

try:
    user1 = int(input("Enter a value here: "))
    user2 = int(input("Enter your second value here: "))
    print(user1 / user2)
except ZeroDivisionError:
    print("[x_x] Something seems wrong in your inputs")
except ValueError:
    print("[x_x] Please enter values in integer format only")
