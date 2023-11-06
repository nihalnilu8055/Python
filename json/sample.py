#loads

import json
s='{"name":"abc","age":10}'
d=json.loads(s)
print(type(d))

#dumps

# import json
# d={"name":"abc","age":10}
# l=[1,2,3,4,5]
# t=('a','b','c')
# s={1,2,3,4}

# a=json.dumps(d)
# b=json.dumps(l)
# c=json.dumps(t)
# d=json.dumps(list(s))

# print(a)
# print(b)
# print(c)
print(d)