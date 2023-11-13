#fact(5)=5*fact(5-1)

def fact(num):
    if(num==1):
        return 1
    else:
        return num*fact(num-1)


print("Enter the number to check the factorial value :")
print(fact(int(input())))