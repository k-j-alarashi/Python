try:
    num = int(input("Enter Number : "))
    print(num)
    5/0
    
except ValueError:
    print("Invaild Input ..!")
    
except ZeroDivisionError:
    print("Divide By Zero ..!")
