"""Rental cars tasks using certain list functions and tells people if cars are booked and stuff like that"""
"""cars = []
car = ["Renault", 15000]
cars.append(car)
print(cars)"""



#starts the program
cars = [["Suzuki Van", 2, False], ["Toyota Corlla", 4, False], ["Honda CRV", 4, False], ["Suzuki Swift", 4, False], ["Mitsibishi Airtrek", 4, False], ["Nissan DC Ute", 4, False], ["Toyota Previa", 7, False], ["Toyota High Ace", 12, False], ["Toyota High Ace", 12, False]]
loop = True
chungus_loop = True


#allows the ablilty to loop through the rental multiple times
while chungus_loop == True:
    #starts the gui
    loop = True
    while loop == True:
        try:
            #asks for the amount of seats the user needs
            seats = int(input("Please enter the number of seats required (type '-1' to quit):\n"))
            #checks if the user entered the kill command and stops the loops and goes to the bottom
            if seats == -1:
                chungus_loop = False
                break
            elif seats <= 0:
                print("Please put in a number greater than 0 as you count as 1") 
                print()
            elif seats >= 13:
                print("Sorry their aren't any cars with more than 12 seats")
                print()            
            else:
                print()
                loop = False                
        except:
            print("Please enter a valid number")
    
    #finsihes the full break of the loops
    if seats == -1:
        chungus_loop = False
        break    
    #prints the list of cars the user is able to have
    for b in range(0, 9):
        if cars[b][1] >= seats and cars[b][2] == False:
            print("No.", b + 1, "-", cars[b][0], "with", cars[b][1], "seats")
    
    #restarts the loop
    loop = True
    
    
    #prints a gap
    print()
    
    #starts up another loop to see what car the user would wish to book according to the last loop
    while loop == True:
        try:
            book = int(input("Please enter the a number according to what car you wish to book:\n"))
            if book > 9:
                print("We only have up to 9 cars please put in a lower number")
                print()
            elif book < 1:
                print("Sorry we don't have less than 1 car you egg")
                print()
            elif cars[book][2] == True:
                print("Sorry but that car is already booked")
                print()
            else: 
                cars[book - 1][2] = True
                name = input("What is your name:\n")
                cars[book - 1].append(name)
                print(cars[book - 1][0], "has been booked by", name)
                loop = False
        except:
            print("Please select a valid number") 

#this is after the chungus_loop and will print to the admin after they enter the finish command and tell them which vehicles have been borrowed 
print()
print("Vehicles booked today:")
for i in range(0, 9):
    if cars[i - 1][2] == True:
        print(cars[i - 1][0], "- Booked by:", cars[i - 1][3])