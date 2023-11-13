# Different display mechanishm

print("Hello") #After executing the display control goes to next line.
print("World...") # It will print as Hello ENTER World...
print()
print("Hello",end=' ') #After execute this statement end with hold it with blank space inline
print("World...")

# here , means separators in print statement. And which default value is "White Space"
# But we can manually enter value to it. Let's check
d=12
m=11
y=2022
print("Today's Date is :",d,m,y) # print as 12 11 2022
#But
print("Todays Date is :",end=' ')
print(d,m,y,sep='/')        #Print as 12/11/2022

