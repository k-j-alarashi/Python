letter = ['a' , 'd' , 'h' , 'l']


def search(s):
    for i in letter:
        if (i==s):
            print("found")
            break
    else:
        print("not found")


element = input("Enter Element to Search : ")
search(element)