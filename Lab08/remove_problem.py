letter = ['a' , 'b' , 'c']

print(letter)

for i in letter:
    letter.remove(i)
    print(letter)
# لم يتم حذف b ?

# لان letter تعطي i في اول دورة في for العنصر الموجود في الموقع 0 فيصبح شكل list كالتالي :
# ['b', 'c']

# الان اصبح b في الموقع 0 بعد حذف a ، ولكن في الدورة الثانية تعطي letter العنصر الموجود في العنوان 1 لل i وهو c ثم يتم حذفه
# ['b']