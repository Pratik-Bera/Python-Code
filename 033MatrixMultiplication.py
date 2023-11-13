# Matrix Multiplication

import copy

print("Enter The Dimention of Matrix:")
dim=int(input())
list1=[]
temp_list=[]
print("Enter the Ekements To make 1st matrix...")
for i in range(dim):
    for j in range(dim):
        print("Enter The Element")
        temp_list.append(int(input()))
    list1.append(copy.deepcopy(temp_list))
    temp_list.clear()



list2=[]
print("now, Enter the Ekements To make 2nd matrix...")
for i in range(dim):
    for j in range(dim):
        print("Enter The Element")
        temp_list.append(int(input()))
    list2.append(copy.deepcopy(temp_list))
    temp_list.clear()

print("Your 1st matrix is :")
print(list1)
print("Your 2nd matrix is :")
print(list2)

mul_list=[]
for i in range(dim):
    for j in range(dim):
        temp_list.append(int(0))
    mul_list.append(copy.deepcopy(temp_list))
    temp_list.clear()

for i in range(dim):
    for j in range(dim):
        for k in range(dim):
            mul_list[i][j]=mul_list[i][j]+list1[i][k]*list2[k][j]
print("The multiplication result is :")
print(mul_list)

