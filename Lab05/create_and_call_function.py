def show():
    print("Hello From Function ...")
    
# call
show()

def greet(name="Guest"): # name ---> local variable ( متغير محلي معرف على مستوى الدالة فقط )
    print("Hi ",name)

# اذا ارسل المستخدم قيمة للدالة يأخذها ويتجاهل ( Guest )
name = input("Enter Name : ")
greet(name)
print("====================")
# اذا لم يرسل المستخدم قيمة للدالة وكانت الدالة تستقبل parameter بشكل اختياري فانه يأخذ القيمة الافتراضية
greet()