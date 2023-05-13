def binary_search(a,x):
    l=0
    h=len(a)-1
    m=0
    
    while(l<=h):
        m = (h+l)//2
    
        if a[m]<x:
            l=m+1
        elif a[m]>x:
            h=m-1
        else:
            return m
    return -1

array = [1,2,2,4,5,5,6,7]

search = 4

index = binary_search(array,search)
if index == -1:
    print("Search element is not found ")
else:
    print("Search element is found at index : ",index)