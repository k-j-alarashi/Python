a = {1,2,3,7}
b = {1,2,3,4,5}

print("اتحاد : ",a.union(b))
print("تقاطع : ",a.intersection(b))
print("هل a مجموعة جزئية من b : ",a.issubset(b))
print("هل a مجموعة شاملة من b : ",a.issuperset(b))
print("هل b مجموعة شاملة من a : ",b.issuperset(a))
print("العناصر الموجودة في b و غير موجودة في a : ",b.difference(a))
print("العناصر الغير مشتركة بين المجموعتين : ",a.symmetric_difference(b))
