# factorial program using while loop

print("Enter The Number to Check It's Factorial Value :")
num=int(input())
ans=1;
while(num>=1):
    ans=ans*num
    num-=1

print("The Factorial result is : ",ans)
