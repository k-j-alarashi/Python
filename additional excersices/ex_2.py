num = int(input("Enter Number : "))
sum_even = 0
sum_odd  = 0

for i in range(1,num+1):
    if (i%2==0) :
        sum_even = sum_even + i
    else:
        sum_odd += i
print("===============================")
print("sum of even numbers : ",sum_even)
print("sum of odd  numbers : ",sum_odd)
print("===============================")