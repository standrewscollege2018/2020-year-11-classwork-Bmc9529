""" this program is used for making a madlib sentence, in this cause its going to be making excuses to geet out of whatever the user wants"""

#introdruces the user to the program
print("Welcome lazy one, obviously you can't be stuffed to do something today,:")
print("so your lazy ar*e came here, to make an excuse to get out of it")

#gets inputs of the variaty of things needed
name = input("Please not that I care but however I require your name: ")
body = input("Righty oh, now I require a body part affected for your excuse: ")
illness = input("Now what type of illness do you 'have': ")
escaping = input("What is the thing you don't want to do: ")
days = input("How many days are you meant to get out: ")
email = input("Email of the recipient: ")

#sees if the users wants to get attacked by a animal
animal = input("Do you want to be attacked by an animal. If yes type 'yes' otherwise 'no': ")

#goes through a variable checker for the past variable 
if animal == "yes":
    print()
    print("My wife and I are sorry to inform you but {} has recently been attacked by a {}.".format(name, animal))
    print("In doing so", name,"'s", "brain came out of their skull. Luckly", name, "survied said attack,")
    print("but as his brain rubbed all over the ground infecting", name, "with", illness,".")
    print("The doctors where unable to save", name, "unless they took cells from", body,)
    print("meaning that he is unable to do", escaping, "as the doctors have locked him in an insane asylum for",days,"days")
    print("This is because anyone that was to actually think that this program would convince someone to let", name, "out")
    print("of", escaping, "would have to be chronically insane")
    print("Thanks")
    print("")
    print("Some Random Program")
    print()
    print("sending to", email)
    print("sent...")
    print("have a nice day")

elif animal == "Yes":
    print()
    print("My wife and I are sorry to inform you but", name, "has recently been attacked by a", animal,".",)
    print("In doing so", name,"'s", "brain came out of their skull. Luckly", name, "survied said attack,")
    print("but as his brain rubbed all over the ground infecting", name, "with", illness,".")
    print("The doctors where unable to save", name, "unless they took cells from", body,)
    print("meaning that he is unable to do", escaping, "as the doctors have locked him in an insane asylum for",days,"days")
    print("This is because anyone that was to actually think that this program would convince someone to let", name, "out")
    print("of", escaping, "would have to be chronically insane")
    print("Thanks")
    print("")
    print("Some Random Program")
    print()
    print("sending to", email)
    print("sent...")
    print("have a nice day")    
    
else:
    print()
    print("My wife and I are sorry to inform you but", name, "recently had an accident that caused him to fall over and")
    print("split his skull open, this meant", name,"'s", "brain rubbed all over the ground infecting", name, "with", illness,".")
    print("The doctors where unable to save", name, "unless they took cells from", body,)
    print("meaning that he is unable to do", escaping, "as the doctors have locked him in an insane asylum for",days,"days")
    print("This is because anyone that was to actually think that this program would convince someone to let", name, "out")
    print("of", escaping, "would have to be chronically insane")
    print("Thanks")
    print("")
    print("Some Random Program")
    print()
    print("sending to", email)
    print("sent...")
    print("have a nice day")    
    
    