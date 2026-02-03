letter = ['a' , 'd' , 'h' , 'l']

# هذه الدالة تستقبل العنصر المراد البحث عنه ( s ) و ايضا المصفوفة list التي نريد البحث فيها
def search(s , myList):
    if s in myList:
        print("found")
    else:
        print("not found")


element = input("Enter Element to Search : ")
search(element , letter)