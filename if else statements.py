""" This is a bit of code that deals with conditionals e.g. if, else statements by seeing if a child is fine for the child price"""

#sets child age limit
child_age = 13

#asks for age of the user the \n creates a new line for the user
age = int(input("What is your age:\n"))

#checks the age and runs the user through a if statement
if age <= child_age:
    print("You pay the child price")
else:
    print("Sorry you do not met the age requirements for the child price")

#just prints a wlecoming after the if statement
print()
print("Welcome to the zoo")
