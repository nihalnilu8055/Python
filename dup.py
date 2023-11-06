# a=["a","b","m","a","c","a","b"]
# b=[]

# for i in a:
#     if a.count(i)>1:
#         b.append(i)
# d=set(b)
# f=list(d)
# print(f)


# lis = ["a","b","m","a","c","a","b"]


# dup= []

# for i in lis:
# 	if i not in dup:
#             dup.append(i)


# print(dup)


# list= ["a","b","m","a","c","a","b"];     
     
    
# for i in range(0, len(list)):    
#     for j in range(i+1, len(list)):    
#         if(list[i] == list[j]):    
#             print(list[j]); 
# # print("Duplicate : ");  



list = ["a","b","m","a","c","a","b"]
new = [] 
for a in list:
	n = list.count(a)
	if n > 1:
		if new.count(a) == 0: 
			new.append(a)
print(new)