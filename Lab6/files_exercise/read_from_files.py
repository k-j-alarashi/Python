# عندما يكون mode="r" ضروري ان يتم انشاء الملف مسبقا
file = open("names.txt" , "r")
for i in file:
    print("Name  : ",i)
file.close()

# دالة read() تقرأ كل محتوى الملف مرة واحد
# file = open("names.txt" , "r")
# print(file.read())
# file.close()

# دالة readline() تقرأ سطر واحد فقط من الملف
# file = open("names.txt" , "r")
# print(file.readline())
# print(file.readline())
# file.close()

# دالة read() تقرأ كل محتوى الملف وترجعه على شكل list
# file = open("names.txt" , "r")
# print(file.readlines())
# file.close()