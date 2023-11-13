# Reverse of It's Digits
print("Enter a Number To Convert it into Reverse :")
num=int(input())
count=0
rev=0
if(num<0):
    num=abs(num)
    count+=1
while(num>0):
    r=num%10
    num=num//10
    rev=rev*10+r
if(count==0):
    print("Revarse Number is : ",rev)
else:
    print("Revarse Number is : ",(rev*(-1)))
