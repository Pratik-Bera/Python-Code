# Printing Formation
num=2
for i in range(1,11):
    print(num," X ",i," = ",num*i)      #Simle way
print()

for i in range(1,11):
    print(f'{num} X {i} = {num*i}')     # It's f string Formmating
print()

for i in range(1,11):
    print("{0} X {1} = {2}".format(num,i,(num*i)))  # .format formatting with number.
print()

for i in range(1,11):
    print("%d X %d = %d"%(num,i,num*i))    # C Formmatting
print()

pi=22/7
print(pi)       # That will print 3.142857142857143
print("%f"%(pi))
# But we want to show 2 digits after point.
#1.
print('%.2f'%(pi))
#2
print(f'{pi:.2f}')
#3.
print("{0:.2f}".format(pi))

