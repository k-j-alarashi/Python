# تضمين مكتبة بكل محتوياتها في البرنامج
# import random   # ex ----> index = random.randint(0,2)

# الطريقة الثانية من الممكن تضمين المكتبة ثم نرمز لها بمتغير
import random as r # ex ----> index = r.randint(0,2)

# الطريقة الثالثة هي تضمين الدالة التي احتاجها فقط وليس كل المكتبة
# from random import randint  # ex ----> index = randint(0,2)

letter = ['a' , 'b' , 'c']

index = r.randint(0,2)

print(letter[index])