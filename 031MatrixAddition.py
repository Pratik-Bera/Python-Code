# This is matrix addition Program.
import copy
print("Enter The Dimention of Matrix :")
dim=int(input())

list1=[]
temp_list=[]
for i in range(1,dim*dim+1):
    print("Enter the element for",i)
    temp_list.append(int(input()))
    if(i%dim==0):
        list1.append(copy.deepcopy(temp_list))
        temp_list.clear()


list2=[]
print("Now, Enter your 2nd list :")
for i in range(1,dim*dim+1):
    print("Enter the element for",i)
    temp_list.append(int(input()))
    if(i%dim==0):
        list2.append(copy.deepcopy(temp_list))
        temp_list.clear()

print("Your 1st list is : ")
print(list1)
print("Your 2nd list is : ")
print(list2)

added_list=[]
for i in range(dim):
    for j in range(dim):
        temp_list.append(list1[i][j]+list2[i][j])
    added_list.append(copy.deepcopy(temp_list))
    temp_list.clear()

print("Matrix added list is :")
print(added_list)




