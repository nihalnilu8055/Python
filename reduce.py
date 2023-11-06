
# l=[1,2,3,4,5,6,7,8,9,10]
# def sample(*abc):
#     return abc[0]+abc[1]
# print(reduse(sample,l))



# import functools
# lis = [1, 3, 5, 6, 2]
# print("The sum of the list elements is : ", end="")
# print(functools.reduce(lambda a, b: a+b, lis))
# print("The maximum element of the list is : ", end="")
# print(functools.reduce(lambda a, b: a if a > b else b, lis))




def reduce(function, iterable, initializer=None):
	it = iter(iterable)
	if initializer is None:
		value = next(it)
	else:
		value = initializer
	for element in it:
		value = function(value, element)
	return value
tup = (2,1,0,2,2,0,0,2)
print(reduce(lambda x, y: x+y, tup,6))

