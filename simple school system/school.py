import os
def addStudent(id,name,major,avg):
    try:
        f = open("students.txt" , "a")
        f.write(str(id)+"\n")
        f.write(name+"\n")
        f.write(major+"\n")
        f.write(str(avg)+"\n")
        f.close()
        print("				SAVED SUCCESSFULLY ...")
    except:
        print("				NOT SAVED ...")

def display():
    f = open("students.txt" , "r")
    for i in f:
        print("ID        : "+i.rstrip())
        i = f.readline()
        print("NAME      : "+i.rstrip())
        i = f.readline()
        print("MAJOR     : "+i.rstrip())
        i = f.readline()
        print("AVG       : "+i.rstrip())
        print("-----------------")
    f.close()

def search(id):
    f = open("students.txt" , "r")
    for i in f:
        if(i.rstrip()==id): # i = 1111\n  id  =1111
            print("ID        : "+i.rstrip())
            i = f.readline()
            print("NAME      : "+i.rstrip())
            i = f.readline()
            print("MAJOR     : "+i.rstrip())
            i = f.readline()
            print("AVG       : "+i.rstrip())
            print("-----------------")
            break
    else:
        print("				NOT FOUND ...")
    f.close()

# (temp) عند تنفيذ عمليتي التعديل أو الحذف على الملفات في بايثون، يتم الاعتماد على ملفٍ وسيط 
# حيث تُنقل جميع البيانات من الملف الأصلي إلى هذا الملف، مع تعديل السجلات المطلوبة أثناء النقل، أو تجاهل السجلات المراد حذفها.
# وبعد الانتهاء، يُستبدل الملف الأصلي بالملف الوسيط.

def updateStudent(id):
    try:
        f = open("students.txt" , "r")
        temp = open("temp.txt" , "a")
        found = False
        for i in f:
            if (i.rstrip()==id) :
                found = True
                name = input("Enter New Name  : ")
                major = input("Enter New Major : ")
                avg = float(input("Enter New Avg   : "))
                temp.write(str(id)+"\n")
                f.readline()
                temp.write(name+"\n")
                f.readline()
                temp.write(major+"\n")
                f.readline()
                temp.write(str(avg)+"\n")
            else:
                temp.write(i)
                i = f.readline()
                temp.write(i)
                i = f.readline()
                temp.write(i)
                i = f.readline()
                temp.write(i)
        f.close()
        temp.close()
        os.remove("students.txt")
        os.rename("temp.txt" , "students.txt")
        if found:
            print("				UPDATED SUCCESSFULLY ...")
        else:
            print("				NOT FOUND ...")
    except:
        print("				NOT UPDATED ..!")


def deleteStudent(id):
    try:
        f = open("students.txt", "r")
        temp = open("temp.txt", "a")
        found = False

        for i in f:
            if i.rstrip() == id:
                found = True
                # تجاوز سجل الطالب بالكامل
                # تم تجاوز id عند الدخول ال for
                f.readline() # تجاوز name
                f.readline() # تجاوز major
                f.readline() # تجاوز avg
            else:
                temp.write(i)
                temp.write(f.readline())
                temp.write(f.readline())
                temp.write(f.readline())

        f.close()
        temp.close()

        if found:
            import os
            os.remove("students.txt")
            os.rename("temp.txt", "students.txt")
            print("				DELETED Successfully ...")
        else:
            print("				NOT FOUND ...")

    except:
        print("				NOT DELETED ..!")


while (True) :
    choice = int(input('''
                                (-: School Managment System :-)
                               _________________________________
                                       Enter Your Choice :
                               =================================
                                1 ) Add.
                                2 ) Display.
                                3 ) Search.
                                4 ) Update.
                                5 ) Delete.
                                6 ) Exit.
                               =================================
    '''))
    match choice :
        
        case 1:
            print("    Enter Student Information    ")
            print("---------------------------------")
            id = int(input("Enter Student ID    : "))
            name = input("Enter Student Name  : ")
            major = input("Enter Student Major : ")
            avg = float(input("Enter Student Avg   : "))
            addStudent(id,name,major,avg)
            print("=================================")
            
        case 2:
            print("=================================")
            display()
            print("=================================")
            
        case 3:
            print("=================================")
            id = input("Enter Student ID to Search : ")
            search(id)
            print("=================================")
            
        case 4:
            print("=================================")
            id = input("Enter Student ID to Update : ")
            print("---------------------------------")
            updateStudent(id)
            print("=================================")
            
        case 5:
            print("=================================")
            id = input("Enter Student ID to Delete : ")
            print("---------------------------------")
            deleteStudent(id)
            print("=================================")
        
        case 6:
            break
        
        case _:
            print("Invaild Input ...")
            print("=================================")

