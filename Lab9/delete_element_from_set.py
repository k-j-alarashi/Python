mySet = {1 , 'a' , 'b' , 20 , True , 3.5}
print(mySet)
# حذف عنصر عشوائي
print(mySet.pop())

# حذف عنصر محدد
# mySet.remove('a') # تظهر خطأ اذا كان العنصر غير موجود

# حذف عنصر محدد
mySet.discard('a') # لا تظهر خطأ اذا كان العنصر غير موجود

# حذف كل العناصر
# mySet.clear()

print(mySet)