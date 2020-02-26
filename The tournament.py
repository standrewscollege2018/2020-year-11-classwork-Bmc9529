"""Calculates the points in a tournament using list, loop, variables and try and except functions"""

#sets the while loop and any variables
loop = True
loop_in_loop = True
opponents = []
wins = 0
draws = 0
loses = 0

#Welcomes them to the program
print("Welcome to the super tournament win calculator")

#for a space
print()

#gets input from user
team = input("Enter your team name:\n")

print()
print("** Oppenents **")
print()

#gets oppents from user
while loop == True:
    A = input("Please enter opponents names:\n")
    if A.lower() == "done":
        print()
        loop = False
    else:
        opponents.append(A)
        
print("** Results **")
loop = True
print()
while loop == True:
        for i in range(len(opponents)):
            print("Game versus {} {}".format(opponents[i], i + 1))
            loop_in_loop = True
            while loop_in_loop == True:
                try:
                    score_home = int(input("{} score:\n".format(team)))
                    score_away = int(input("{} score:\n".format(opponents[i])))
                    if score_away < 0 or score_home < 0:
                        print()
                        print("Please put in a number higher than 0\n")                        
                    elif score_away == score_home:
                        print("You drew\n")
                        draws += 2
                        loop_in_loop = False
                    elif score_home > score_away:
                        print("You won\n")
                        wins += 3
                        loop_in_loop = False                        
                    else:
                        print("You lost\n")
                        loses += 1
                        loop_in_loop = False
                except:
                    print()
                    print("Please enter a vaild number\n")                
        loop = False

print("Competition complete!")
print(team, "finsihed the competition with {} points".format(wins + draws + loses))