l1=[['987qwe','752sdf'],
    ['123abc','456efg']]
c=[]
for i in l1:
    c=i
    for i in c:
        for j in i:
            if j.isdigit():
                print(j)