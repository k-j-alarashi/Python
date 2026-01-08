# print the following shape using loop.
# 1 2 3 4 
# 1 2 3 
# 1 2 
# 1 

for i in range(4,0,-1):
    for j in range(1,i+1):
        print(j , end=' ')
    print()
