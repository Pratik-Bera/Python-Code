import ImportingFun
l1=list(range(0,51))
print("Enter your number :")
num=int(input())
if(ImportingFun.obvious_Search(l1,num)==True):
    print("Your number is available in the entire list.")
else:
    print(" Your number isn't available in list. Thank you.")
print(l1)