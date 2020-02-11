"""tells the user what the price of movie tickets is by getting their age and if they are a student"""

#sets a variable for the age of the user
age = float(input("What is your age:\n"))

#puts a gap
print()

if age >= 13:
    #ask if the user is a student or not
    student = input("Are you a student, if so type your email to confirm, else please write 'N/A'\n")

#gap
if student == "N/A" or age < 13:
    if age >= 18:
        print("Tickets are $12")
    elif age >= 13 and age < 18:
        print("Tickets are $9")
    elif age >= 5 and age < 13:
        print("Tickets are $7")
    else:
        print("Tickets are free!!!")


#goes through the student prices
else: 
    print("Prices are $8")