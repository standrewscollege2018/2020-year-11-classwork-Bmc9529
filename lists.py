"""using list functions to tell the user the mean of the numbers"""
#starts the while functions
loop = True

numbers = []

while loop == True:
        a = float(input("Enter a positive number:\n")) 
        if a == -1:
                loop = False
                print("You entered these numbers")
                for i in range(len(numbers):
                               print(numbers[i])
                print("The mean is", sum(numbers) / len(numbers)
        elif a < 0:
                print("Enter a positive number")
        else:
                numbers.append(a)