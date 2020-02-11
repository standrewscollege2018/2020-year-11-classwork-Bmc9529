"""Calculates the amount of paracetamol a patitent needs based on their weight and age"""

#minium age for the two 500g tablets 
min_age = 12

#ask for the age of patient
age = int(input("What is the patient's age:\n"))

#puts in a visual spacer
print()

if age >= min_age:
    print("Patient is eligible for two tabelts of 500g worth of paracetamol within each 4-6 hours")
elif age < 0:
    print("Age has to be higher than 0")
else:
    #ask for the weight as it is only important in this point of age
    weight = float(input("What is the weight of the patient:\n"))
                   
    print("The patient requires {}g of paracetamol every 4-6 hours".format(weight * 10))
    