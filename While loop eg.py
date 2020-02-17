""" While loop examples"""

#set boolean to true
keep_asking = True

#start asking to guess a number
while keep_asking == True:
    number = int(input("Guess a number:\n"))
    if number == 10:
        keep_asking = False
    else:
        print("Wrong number")
#loop finishes 
print("Correct number")