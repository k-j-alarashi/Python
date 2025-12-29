def addStudent(id,name,major,avg):
    try:
        f = open("students.txt" , "a")
        f.write(str(id)+"\n")
        f.write(name+"\n")
        f.write(major+"\n")
        f.write(str(avg)+"\n")
        f.close()
        print("			Saved Successfully ...")
    except:
        print("			Not Saved ...!")

def display():
    f = open("students.txt" , "r")
    for i in f:
        print("ID           : ",i.rstrip())
        i = f.readline()
        print("NAME         : ",i.rstrip())
        i = f.readline()
        print("MAJOR        : ",i.rstrip())
        i = f.readline()
        print("AVG          : ",i.rstrip())
        print("-----------------")
    f.close()

def search(id):
    f = open("students.txt" , "r")
    for i in f:
        if(i.rstrip()==id):
            print("ID           : ",i.rstrip())
            i = f.readline()
            print("NAME         : ",i.rstrip())
            i = f.readline()
            print("MAJOR        : ",i.rstrip())
            i = f.readline()
            print("AVG          : ",i.rstrip())
            print("-----------------")
            break
    else:
        print("No Student ...!")
    f.close()

while (True) :
    choice = int(input('''
                        Enter Your Choice :
                        ===================
                        1 ) Add.
                        2 ) Dispaly.
                        3 ) Search.
                        4 ) Exit.
    '''))
    match choice:
        case 1:
            id = int(input("Enter student id : "))
            name = input("Enter student name : ")
            major = input("Enter student major : ")
            avg = float(input("Enter student average : "))
            addStudent(id,name,major,avg)
            print("=================================")
        case 2:
            display()
            print("=================================")
        case 3:
            id = input("Enter student id : ")
            search(id)
            print("=================================")
        case 4:
            break
        
        
        