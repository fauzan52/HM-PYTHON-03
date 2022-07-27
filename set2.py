set1 = {1,2,3}
set2 = {4,5,6}
set2.add(90)
set1.update(set2)
print (set1)
set3 = {1,2}
print(set3.issubset(set1))
print(set1.issuperset(set3))
# if set3.issubset(set1) :
#     print ('subset')
# else :
#     print ('bukan subset')