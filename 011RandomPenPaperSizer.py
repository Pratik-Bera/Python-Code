#Stone paper Sizer game using list if else and random import

import random

a=random.randrange(1,4)
a2=["STONE" , "PAPER" , "SIZER"]
print("Select Your Option :")
print("1.STONE  2.PAPER  3.SIZER")
ui=int(input())
if((ui<=1)and(ui>=3)):
    print("Input Invalid. Try Again")
elif(ui==a):
    print("Computer Coosen",a2[a-1]," So, Match Tie.")
elif((ui==1)and(a==2)):
    print("Computer Choose PAPER . So you LOST. Try Again.")
elif((ui==2)and(a==3)):
    print("Computer Choose SIZER.So You LOST.Try Again.")
elif((ui==3)and(a==1)):
    print("Computer Choose STONE.So You LOST.Try Again.")
else:print("Congrats! YOU WON. Computer was choosen ",a2[a-1])
# print(a)

  


