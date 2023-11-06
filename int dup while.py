# list=[int(x) for x in input("enter a list: ").split()]
# i=0
# while i<len(list):
#     j=i+1
#     while j<len(list):
#         if list[i]==list[j]:
#             list.pop(j)
#         else:
#             j +=1
#     i+=1
# print(list) 





input=input("enter a list: ")
list=input.split()
a=[]
for i in list:
    a.append(int(i))
result=[]
i=0
while i<len(a):
    if a[i] not in result:
        result.append(a[i])
    i+=1
print(result)        