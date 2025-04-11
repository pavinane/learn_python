# tuple : allow duplicate but it can't modify , add,or delete
#  but it can change to list can modify , add or delete

a=(1,2,3,4,5)
print (a)
b = list(a)
b.pop()
print (b)