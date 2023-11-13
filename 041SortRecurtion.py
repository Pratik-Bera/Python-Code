# This is an sorting algorithm using recurtion.

def findmini(l1):
    mini=l1[0]
    for i in range(len(l1)):
        if(l1[i]<mini):
            mini=l1[i]
    return mini


def listsorter(l1):
    if(len(l1)<=1):
        l2.append(l1)
        return l1
    minele=findmini(l1)
    l2.append(minele)
    l1.remove(minele)
    listsorter(l1)
    return l2


listmain=[2,5,1,8,9]
l2=[]
ordered_list=listsorter(listmain)
print(ordered_list)