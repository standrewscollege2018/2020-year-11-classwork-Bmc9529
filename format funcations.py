"""transforms gigabytes to megabytes using the .format() function"""

#tells the use what it can do
print("I can tell you have many Mb in a Gb")

#changing variable so its in lowercase and ask for user input
gb = float(input("How many Gb: "))

#constant variable so its in caps
MB = 1024

#prints the result
print("There are {}Mb in {}Gb".format(gb * MB, gb))
                                      
                                      
                                      