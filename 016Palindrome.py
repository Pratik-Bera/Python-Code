# Check The number is Palindrome or not ?

print("Enter a Number To Chech Is That Palindrome")
num=abs(int(input()))
num2=num;
rev=0
while(num>0):
    r=num%10
    num=num//10
    rev=rev*10+r
if(rev==num2):
    print("It's Palindrome !")
else:
    print("It's Not Palindrome.")