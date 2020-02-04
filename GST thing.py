#if their input is yes it will go to remove gst otherwise add
inpt = input("Do you want to remove GST: ")


if(inpt = yes):
   item_name = input("Item name?: ")
   item_price = float(input("Item price?: "))
   print("The", item_name, "will cost","$", item_price / 1.15, "excluding GST")
else:
   #ask for name of item
   itm_name = input("Item name?: ")
   
   #ask for price of item
   itm_price = float(input("Item price?: "))
   
   #prints name and price inc of GST
   print("The car will cost","$", itm_price * 1.15, "including GST")   
