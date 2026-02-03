from datetime import date
products = (
    [1 , "Coffee" , 200],
    [2 ,  "Tea"   , 100],
    [3 , "Juice"  , 150]
    )

invoice_num = 1
customer_products = []


def display():
    print("						============PRODUCTS==============")
    print("						ID          NAME          Price")
    print("						----------------------------------")
    for p in products:
        print(f"						{p[0]:<12}{p[1]:<14}{p[2]:<4}YR")
    print("						==================================")



def Sale(pid , qty):
    global customer_products , products
    for p in products:
        if p[0]==pid:
            customer_products.append([products[pid-1][1] , qty , products[pid-1][2] , products[pid-1][2]*qty])
            print("Done ...")
            break
    else:
        print("Product Not Found ..!")



def PrintInvoice():
    global customer_products , invoice_num
    total = 0
    print(f'''
=========================================================
                        INVOIVE
=========================================================
Invoice no : {invoice_num}
DATE       : {date.today()}
---------------------------------------------------------
Item           Qty         Item Price         Price Total
=========================================================''')
    for p in customer_products:
        print(f"{p[0]:<14} {p[1]:<11} {p[2]:<18} {p[3]:<5}YR")
        total = total + p[3]
    print("---------------------------------------------------------")
    print(f"Total : {total} YR ")
    print("=========================================================")
    print(" 		     ❁ Thank You ❁				")
    print("=========================================================")
    customer_products.clear()
    invoice_num+=1

display()

while True :
    c = input('''
Enter Your Choice :
1 ) Display Products.
2 ) Sale Products.
3 ) Print Invoice.
4 ) Exit
''')
    match c:
        case "1":
            display()
        case "2":
            while True:
                pid = int(input("Enter The Number  of product : "))
                qty = int(input("Enter The Quntity You Want   : "))
                Sale(pid , qty)    
                c = input("Press ( y or Y ) to buy more , or ( e or E ) to exit : ").lower()
                print("_____________________________________________________________________________")
                if c=="e":
                    break
        case "3":
            PrintInvoice()
        case "4":
            break
        case _:
            print("error ..!")
    
 
    
    
