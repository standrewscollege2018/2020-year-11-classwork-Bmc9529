"""code for making a silent auction using while loops and more using a practical approach"""

#sets the keep asking functions
keep_betting = True
keep_start = True

#sets other varibles 
highest_bid = 0



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

#prints a gap
print()

while keep_betting == True:
    try:
        name = input("What is your name?\n")
        bid = float(input("What is your bid?\n"))
        if name == "admin" and bid == -1 and highest_bid >= admin_res:
            keep_betting = False
        elif name == "admin" and bid == -1 and  highest_bid <= admin_res:
            
        if bid > highest_bid:
            highest_bid = bid
            highest_name = name
            print("highest bid so far is {} with ${}".format(highest_name, highest_bid))
            #gap
            print()
        else:
            print("Sorry {} Please enter a higher bid".format(name))
            print("highest bid so far is {} with ${}".format(highest_name, highest_bid))
    except:
        print("Please etner a valid bid")
        
print()
print("Thanks for betting. The auction for the {} has finished with a bid of {}".format(admin_auc, highest_bid))
print("Congrats to", highest_name)
            
                    
    
    
        