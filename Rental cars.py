"""Rental cars tasks using certain list functions and tells people if cars are booked and stuff like that"""
"""cars = []
car = ["Renault", 15000]
cars.append(car)
print(cars)"""



#starts the program
cars = [["Suzuki Van", 2, False], ["Toyota Corlla", 4, False], ["Honda CRV", 4, False], ["Suzuki Swift", 4, False], ["Mitsibishi Airtrek", 4, False], ["Nissan DC Ute", 4, False], ["Toyota Previa", 7, False], ["Toyota High Ace", 12, False], ["Toyota High Ace", 12, False]]
loop = True

#starts the gui
while loop == True:
    try:
        seats = int(input("Please enter the number of seats required (type -1 to quit):\n"))
        if seats == -1:
            loop = False
            exit
            quit
        print()
        loop = False
    except:
        print("Please enter a valid number")

#prints the list of cars the user is able to have
for b in range(0, 9):
    if cars[b][1] >= seats and cars[b][2] == False:
        print("No.", b + 1, "-", cars[b][0])

#restarts the loop
loop = True


#prints a gap
print()


while loop == True:
    try:
        book = int(input(
