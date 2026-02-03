def power(base , exp):
    result = 1
    for i in range(1,exp+1): # or range(exp)
        result = result * base
    return result

print(power(2,3))

# طريقة أخرى لحساب الاس
# def power(base , exp):
#     return base**exp
# 
# print(power(2,3))