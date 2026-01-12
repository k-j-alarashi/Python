def add(*nums):
    s = 0
    for i in nums:
        s = s + i
    return s

print(add(1,2,3,4,5,6,7))