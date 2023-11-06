p=float(input('Enter purchase amount '))
if p>=100:
    dis=p*0.1
else:
    dis=0
dis=p-dis
print("the discounted amount is RS",dis)