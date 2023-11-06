# num=[int(x) for x in input("enter a list: ").split()]
# sum=sum(num)
# avg=sum/len(num)
# i=0
# while i<len(num):
#     if num[i]>avg:
#         print(num[i])
#     i+=1    




num_list=[]
input=input("enter a list: ")
num=input.split()
for i in num:
    num_list.append(int(i))
total_sum=sum(num_list)
avg=total_sum/len(num_list)    
i=0
while i<len(num_list):
    if num_list[i]>avg:
        print(num_list[i])
    i+=1    