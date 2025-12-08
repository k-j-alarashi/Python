richter = float(input("Enter The Degree of Richter : "))

if (richter >=8.0):
    print("Destoryed ..!")

elif (richter >= 4.0):
    print("Strong")

elif (richter >= 2.0):
    print("Moderate")

else:
    print("Weak")