def add(num1 , num2):
    result = num1 + num2
    return result

print("result = ",add(3,2))

print("==================")
# دالة ترجع أكثر من متغير

def add2(num1 , num2):
    result = num1 + num2
    return result , num1 , num2

x, y, z = add2(3,2)
print("x = ",x)
print("y = ",y)
print("z = ",z)