# sum of numbers
def sumof(x):
    if(x>0):
        return (x+sumof(x-1))
    else:
        return 0




print("Enter number you want to sum upto")
num=int(input())
result=sumof(num)
print(result)


