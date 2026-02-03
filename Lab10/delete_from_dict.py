myDict = {"id":"20258736459" , "name":"Khaled"}
print(myDict)
# print(myDict.pop("id" , "Error")) # حذف القيمة باستخدام key مع اظهار رسالة "Error" في حالة عدم وجود "key"
print(myDict.popitem()) # حذف اخر item (key+value)
# myDict.clear() # حذف كل items من myDict
print(myDict)