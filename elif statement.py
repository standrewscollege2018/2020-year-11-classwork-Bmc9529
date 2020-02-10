""" deals with doing elif statements for marks """

#asks for the input of marks
mark = int(input("What mark did you get?\n"))

#prints an extra line to make it look better
print()

#goes through the if statemets to see what mark you go
if mark >= 90 and mark <= 100:
    print("Congrats on gettings an A")
elif mark > 100:
    print("Please right your answer as you cant get higher than 100")
elif mark < 0:
    print("Please put your right answer as you couldn't get below 0 in the test")
elif mark < 90 and mark >= 70:
    print("Good job you got a B")
elif mark < 70 and mark >= 50:
    print("Nice work you passed with a C")
else:
    print("Sorry but you failed")
