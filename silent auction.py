"""code for making a silent auction using while loops and more using a practical approach"""

#sets the keep asking functions
keep_betting = True
keep_start = True





#starts the auction
while keep_start == True:
    try:
        admin_auc = input("Enter the item name:\n")
        admin_res = float(input("Please enter the reserve price:\n"))
        keep_start = False
    except:
        print("Please enter a valid reserve price")

#prints a gap
print()


print("The auction for the", admin_auc, "has started!")

#prints a gap
print()

print("The highest bid so far is $0.00")

while keep_betting == True:
    try:
        name = input("What is your name?\n")
        bid = float(input("What is your bid?\n"))
        if name == "admin"
                    
    
    
        