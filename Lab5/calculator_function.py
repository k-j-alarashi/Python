def calculator(num1 , num2 , ops):
    match ops :
        case "+":
            return num1+num2
        case "-":
            return num1-num2
        case "*":
            return num1*num2
        case "/":
            return num1/num2
        case _:
            return "error ...!"

x = int(input("Enter Number : "))
y = int(input("Enter Number : "))
ops = input("Enter the Operations ( + , - , * , / ) : ")
print(calculator(x,y,ops))
        