# This is a grade calculate Program 

print("Enter Student Number : ")
num=int(input())
if((num>100)or(num<0)):
    print("Invalid Input.")
elif(num>90):
    print(" Grade A ")
elif((num<90)and(num>=80)):
    print(" Grade B ")
elif((num<80)and(num>=70)):
    print(" Grade C ")
elif((num<70)and(num>=60)):
    print(" Grade D ")
elif(num<60):
    print(" Grade E ")
