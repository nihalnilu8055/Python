# ip1=input("enter nums:")
# for num in ip1.split():
#     list1=int(num)

# ip2=input("enter nums:")
# for num in ip2.split():
#     list2=int(num)
    
# a=list(set(ip1) & set(ip2))
# print(a)

# ------------------------------------


# l1=[1,2,3,5,9]
# l2=[9,5,2,1,6]
# c=[]
# for i in l1:
#     if i in l2 and i not in c:
#         c.append(i)

# print(c)


# ----------------------------------------


ip1=input("enter no. :")    
ip2=input("enter no. :")

l1=[int(num) for num in ip1.split]
l2=[int(num) for num in ip2.split]

c=[]

for i in l1:
    if i in l2 and i not in c:
        c.append(i)

print(c)


