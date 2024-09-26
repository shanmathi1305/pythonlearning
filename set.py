# set1={1,2,3,4,5}
#print(set1)
# print(type(set1))
#set opertor:
# print(len(set1))


# set2={"apple","banana","orange"}
# set1.update(set2)
# print(set1)
# thisset={"rose","lily","lotus"}
# print("lily"in thisset)
# for i in thisset:
#     print(i)
# i=0

# while i<len (thisset):
#     print(thisset)
#     i+=1
 # add  
# thisset.add("jasmine")
# print(thisset)
# thisset.update("apple")
# print(thisset)

# set1={1,32,35,78}
# set2={4,6,9,7}
# set3=set1|set2
# print(set3)

#remove method:
# set1.remove(32)
# print(set1)
# set1.remove(9)
# print(set1)

#discard method:
# set1.discard(9)
# print(set1)   

# set1.pop()
# print(set1)

# set2={1,4,7,8}
# set3=set1.intersection(set2)
# print(set3)

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# # z = x.difference(y)
# print(z)

#z= x.symmetric_difference(y)
#print(z)
#x.symmetric_difference_update(y)
#print(z)

#z = x.isdisjoint(y)
#print(z)
x = {"a", "b", "c"}
y = {"f", "d", "c", "b", "a}
# z = x.issubset(y)
# print(z)

# z = x.issuperset(y)
# print(z)

z=x.union(y)
print(z)