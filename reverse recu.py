def reverse(s):
    if len(s) <= 1:
        return s
    return s[-1] + reverse(s[:-1])
input= "ootteppetthsi eloom ahtne"
reversed= reverse(input)
print("Org:", input)
print("Reversed:", reversed)