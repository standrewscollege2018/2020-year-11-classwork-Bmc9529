#we need to 'cast', telling the program the data type of the input
number = float(input("Enter a number: "))

#number = int(input("Enter a number: ")) will not work with a Dp. e.g 1.5 but will with whole numbers e.g 1
#number = input("Enter a number: ")) will cause 77 not 14 as you are timesing a string

print("If I times this number by two I get", number * 2)
