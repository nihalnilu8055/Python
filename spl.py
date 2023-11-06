ip="abcdefg!@#$%^&"
op=" "

for i in ip:
    if i.isalnum():
        op += i

print(op)            