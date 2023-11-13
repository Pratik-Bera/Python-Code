# Find The  Number of Digits in a Number

print("Enter a Number for check It's Digit's No :")
# num=abs(int(input()))     # abs Only takes abstract value means - convert into +
num=int(input())
print(num)
count=0
if(num<0):
    num=(num)*(-1)
    

while(num>0):
    num=int(num/10)
    count+=1
print("The Digits No is : ",count)
