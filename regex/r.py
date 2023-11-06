# search(pattern , string ) 
# findall() 

a= r"[a-z]" 
b=r"[A-Z]"
c=r"[0-9]"
d=r"[!@#$%^&]"
password=input("enter password: ")

import re 

if re.search(a,password):
    print("valid")
elif re.search(b,password):
    print("valid")
elif re.search(c,password):
    print("valid")
elif re.search(d,password):
    print("valid")
else:
    print("invalid")



# print() 
# print(re.findall(p,




