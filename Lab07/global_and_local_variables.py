num = 5
name = "a"

def myfun():
    global num , name
    num = 10
    name = "b"
    
myfun()
print(num)
print(name)