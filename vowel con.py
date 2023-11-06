# a=input("enter a char: ")
# b="a","e","i","o","u"
# for i in a:
#     if i in b:
#         continue
#     print(i)


a=input("enter a char: ")
b="a","e","i","o","u"
i=0
while i<len(a):
    if a[i] in b:
        i+=1
        continue
    print(a[i])
    i+=1