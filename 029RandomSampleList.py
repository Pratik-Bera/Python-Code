# Explore Sample Function with list
import random

#example 1
l1=[5,10,40,50,78]
l2=random.sample(l1,3)  # 3 is length of l2 list element taking from l1.
print(l1)
print(l2)

# Example 2   Making a fully random list from a random list.
l3=random.sample(list(range(1000)),50)
print(l3)