"""gets the amount of names a user wants to enter then greats the people the user puts in"""

#gets the amount of names the user wants to enter
number_name = int(input("How many names do you want to enter?:\n"))

#this is for nice lookingness
print()

#does a for loop for the amount of names to get
for i in range(0, number_name):
    name = input("Enter a name: ")
    print(name)