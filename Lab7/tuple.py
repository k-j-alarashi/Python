items_tuple = ("a" , "b" , "c" , "d" , "e" , "f" , 1 , 5.3 , True)
print(type(items_tuple))

temp_list = list(items_tuple)

print("Before  : ")
print("items_tuple --> ",items_tuple)
print("temp_list   --> ",temp_list)

temp_list[0] = "aaa"
items_tuple = tuple(temp_list)

print("==============================")
print("After   : ")
print("items_tuple --> ",items_tuple)
print("temp_list   --> ",temp_list)
