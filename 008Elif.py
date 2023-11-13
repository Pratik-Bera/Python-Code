#Finding Larger Number Between Three Numbers
print("Enter Three Number To Check Large Between Them :")
i1=int(input())
i2=int(input())
i3=int(input())
if(i1<i2):
    if(i3>i2):
        print("The bigger Number is :",i3)
    else:
        print("The bigger Number is :",i2)
elif(i1>i3):
    print("The bigger Number is :",i1)
