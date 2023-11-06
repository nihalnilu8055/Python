password=input("enter ur password: ")
if len(password)<8:
    print("password must be 8 char.")
else:
    uc=False
    lc=False
    digit=False

for i in password:
    if i.isupper():
        uc=True
    elif i.islower():
        lc=True
    elif i.isdigit():
        digit=True
if uc and lc and digit:
    print("password is correct.")
else:
    print("password must be lc, uc and digit.")                                                