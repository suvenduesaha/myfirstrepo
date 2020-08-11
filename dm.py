import copy
a=[1,2,[4,5],3]

b=copy.deepcopy(a)
a.append(9)
print(b)
print(a)