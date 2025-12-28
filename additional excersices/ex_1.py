name = input("Enter Your Name : ")
age  = int(input("Enter Your Age  : "))
avg  = float(input("Enter Your Average : "))

result = ""

if (avg>=75) :
    result = "passed"
else:
    result = "Try Again ..."

print(f'''
===========================
NAME     : {name}
AGE      : {age}
AVGERAGE : {avg}
RESULT   : {result}
===========================
''')