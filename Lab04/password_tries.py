correct_password = "admin"
tries = 1
while (tries <= 3) :
    password = input(f"Enter The Password , try = {tries}")
    if (password==correct_password) :
        print("Login Successfully ...")
        break
    else:
        print(f"Wrong ,Try Again , try = {tries} ")
        tries +=1
else:
    print("No More Tries ..!")
        