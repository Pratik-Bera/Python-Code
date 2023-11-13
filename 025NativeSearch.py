# Native search
import random
l=[]
for i in range(101):
    l.append(random.randint(1,50))
print(l)
print("Enter The Element you wanna search in list :")
element=int(input())
flag=False
for i in range(len(l)):
    if(l[i]==element):
        flag=True
        break
if(flag):
    print(f'The number is in list in {i+1} possitions.')
else:
    print("The Number isn't in the list")
