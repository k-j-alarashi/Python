# def factorial(num):
#     if num==1 or num==0:
#         return 1
#     else:
#         f = 1
#         for i in range(1,num+1):
#             f = f * i
#         return f

def factorial(num):
    if num==1 or num==0:
        return 1
    return num * factorial(num-1)

print(factorial(5))