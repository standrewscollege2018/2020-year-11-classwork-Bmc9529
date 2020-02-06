""" This program gets an item name and price, then adds GST to the price. """

#Lets the user know what the usage for the code is
print("Hello I can calculate GST for you in two ways removing or adding it")

print("")
#if their input is yes it will go to remove gst otherwise add it
inpt = input("Do you want to remove GST (type 'yes' to remove or 'no' to add): ")

#when testing a condition use == not =
if inpt == "yes":
   item_name = input("Item name?: ")
   item_price = float(input("Item price?(please just a number): "))
   print("The", item_name, "will cost","$", round(item_price / 1.15,2), "excluding GST")
else:
   #ask for name of item
   itm_name = input("Item name?: ")
   
   #ask for price of item
   itm_price = float(input("Item price?(please just a number): "))
   
   #prints name and price inc of GST
   #if giving 114.99999999 use the round() code then for more dp put a coma after the calc inside brackets with however many Dp you want
   print("The", itm_name, "will cost","$", round(itm_price * 1.15,2) , "including GST")   
