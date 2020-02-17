""" While loop examples with more stuff"""

#set boolean to true

keep_asking = True
keep_number = True

while keep_asking == True:
    try:
        number = int(input("Guess a number:\n"))
        if number == 10:
                keep_asking = False
        elif number < 10:
            print("Too low, guess again")
        else:
            print("Too high, guess again")
    except:
        print("Error: Invalid number please put in a valid number")
#loop finishes 
print("Correct number")    