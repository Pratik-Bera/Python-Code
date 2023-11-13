# This is binary search without recurtion

def binary_search(l,k):
    begin=0
    end=len(l)-1
    
    while(end-begin>=0):
        mid=(begin+end)//2
        if(k>l[end])or(k<l[begin]):
            return False
        elif(l[mid]==k):
            return True
        elif(l[mid]>k):
            end=mid-1
        elif(l[mid]<k):
            begin=mid+1
        elif(l[begin]==k)or(l[end]==k):
            True
        else:
            return False
        


l=[10,20,30,40,50,60,70,80,90,100]
print(binary_search(l,100))