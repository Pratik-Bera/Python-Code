# Printing the Dot Product of Two vector.

from random import sample

v1=sample(list(range(20)),5)
print(v1)
v2=sample(list(range(50)),5)
print(v2)
dot_product=0

for i in range(len(v1)):
    dot_product=dot_product+v1[i]*v2[i]
print(f'dot product is : {dot_product}')

