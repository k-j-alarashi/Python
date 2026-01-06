# list تقبل انواع مختلفة من البيانات بداخلها
items  = ["a" , "b" , "c" , "d" , "e" , "f" , 1 , 5.3 , True]
# index =  0 ,   1  ,  2  ,  3  ,  4  ,  5  , 6 ,  7  ,  8
#    or
# index = -9 ,  -8  , -7  , -6  , -5  , -4 , -3 , -2 ,  -1

print("Before : ")
print(items)


print("After  : ")
# حذف العنصر في الموقع -5
# items.pop(-5) == items.pop(4)
print(items.pop(-5)) # e
print(items) # ['a', 'b', 'c', 'd', 'f', 1, 5.3, True]


# حذف العنصر 5.3
items.remove(5.3)
print(items) # ['a', 'b', 'c', 'd', 'f', 1, True]

# حذف كل عناصر list
items.clear()
print(items) # []