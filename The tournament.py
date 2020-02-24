"""Calculates the points in a tournament using list, loop, variables and try and except functions"""

#sets the while loop and any variables
loop = True
opponents = []
wins = 0
draws = 0
loses = 0

#Welcomes them to the program
print("Welcome to the super tournament win calculator")

#gets input from user
team = input("Enter your team name:\n")


#gets oppents from user
while loop == True:
    A = input("Please enter opponents names:\n")