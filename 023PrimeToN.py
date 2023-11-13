print ("Enter the Number :")
num=int(input())
if(num<2):
    print("No Output.")
else:
    for i in range(num):
        print(i,end=' ')
        ran=(i//2)+1
        count=0
        for i2 in range(2,ran):
            if((i%i2)==0):
                count=1
        if(count>0):
            print("Not Prime")
        else:
            print("Prime.")    
