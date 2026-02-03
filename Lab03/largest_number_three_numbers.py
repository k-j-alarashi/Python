num1 = int(input("Enter Number : "))
num2 = int(input("Enter Number : "))
num3 = int(input("Enter Number : "))

if num1==num2==num3: #  or ( num1==num2 and num1==num3 )
    print("equals ...")
    
elif num2<=num1>=num3: # or  ( num1 >= num2 and num1 >= num3 )
    print(num1)

elif num2>=num1 and num2>=num3: # or  ( num1<=num2>=num3 )
    print(num2)
    
else :
    print(num3)