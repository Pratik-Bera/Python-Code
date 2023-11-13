# Addition of First n number using For Loop
print("Enter The last range to addition :")
num=abs(int(input()))
ans=0
for i in range(num):
    ans=ans+i
ans=ans+num
print("The result is : ",ans)