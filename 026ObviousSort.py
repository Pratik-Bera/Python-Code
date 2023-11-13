#Obvious Sort is a sort where a list is sorted in another list.

import random
l=[]
for i in range(10):
    l.append(random.randint(0,50))
print(l)
sortedList=[]
while(len(l)!=0):
    min=l[0]
    for i in range(len(l)):
        if(min>l[i]):
            min=l[i]
    sortedList.append(min)
    l.remove(min)
print(sortedList)
        
