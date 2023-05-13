def binary_search(array,search):
    low = 0
    high = len(array)-1
    mid = 0
    
    while low<=high:
        mid = (low+high)//2
        if array[mid]<search:
            low = mid+1
        elif array[mid]>search:
            high = mid-1
        else :
            return mid 
    return -1

array = [1,2,2,4,5,5,6,7]

search = 7

index = binary_search(array,search)
if index == -1:
    print("Search element is not found ")
else:
    print("Search element is found at index : ",index)