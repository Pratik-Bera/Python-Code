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

add_matrix=[]
for i in range(dim):
    for j in range(dim):
        temp_list.append(list1[i][j]+list2[i][j])
    add_matrix.append(copy.deepcopy(temp_list))
    temp_list.clear()

print("Your added matrix is :")
print(add_matrix)
