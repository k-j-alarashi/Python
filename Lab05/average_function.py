def avg(s1, s2, s3):
    result = (s1+s2+s3)/3
    return result

sub1 = float(input("Enter the marks of subject : "))
sub2 = float(input("Enter the marks of subject : "))
sub3 = float(input("Enter the marks of subject : "))
print("====================================")
print("average = ",avg(sub1,sub2,sub3)," % ")
print("====================================")

# من الممكن جعل كل شي داخل الدالة كالتالي :
# def avg2():
#     s1 = float(input("Enter the marks of subject : "))
#     s2 = float(input("Enter the marks of subject : "))
#     s3 = float(input("Enter the marks of subject : "))
#     result = (s1+s2+s3)/3
#     return result
# 
# print("====================================")
# print("average = ",avg2()," % ")
# print("====================================")
