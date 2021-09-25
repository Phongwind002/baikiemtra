listA=[1,1,2,3,5,8,13,21,34,55,88]
listB=[1,3,5,4,7,88,66,59,40,54]
common_l= set (listA) & set (listB)
listC=[];
for i in common_l:
    listC.append(i)
print(listC)
s = set(listA)
print(s)
z = set(listB)
print(z)