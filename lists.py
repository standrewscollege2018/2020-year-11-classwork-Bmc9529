"""using list functions to tell the user the mean of the numbers"""
#starts the while functions
loop = True

numbers = []

while loop == True:
        A = float(input("Enter a positive number:\n")) 
        if A == -1:
                loop = False
                print("You entered these numbers")
                for i in range(len(numbers)):
                        print(numbers[i])
                print("The mean is", sum(numbers) / len(numbers))
        elif A < 0:
                print()
        else:
                numbers.append(A)