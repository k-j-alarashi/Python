# print the following shape using loop.
# 1
# 1 2
# 1 2 3
# 1 2 3 4

for i in range(1,5):
    for j in range(1,i+1):
        print(j , end=' ')
    print()