# def binary_search(list , target):
#     if len(list)==0:
#         return -1
#     list = list.sort()
#     mid = len(list)//2
#     if list[mid] == target:
#         return mid
#     elif list[mid] < target:
#         return binary_search(list[mid+1 : ] , target)
#     else:
#         return binary_search(list[mid-1:], target)
    
# if __name__ == "__main__":
#     list = [1, 3, 5, 7, 9]
#     target = 5

#     index = binary_search(list, target)

#     if index == -1:
#         print("The target is not found.")
#     else:
#         print("The target is found at index", index)

    #  0|1|2|3|4|5|6|7|8|9
arr = [1,2,3,4,5,6,7,8,9,10]
target = 3
def binary_search(arr,low,high,target):
    if low > high :
        #0  10
        #10  5 ==  -1
        return -1
    
    mid = (low+high)//2
    #       0 + 9 == 9 = 9/2 (mid==4)
    if arr[mid]==target: # a[5] == 3 
        return mid
    if arr[mid]>target: # The target is in the left half of the array 5 > 3
        return binary_search(arr , low , mid-1 , target)
    else :# 5<3
        return binary_search(arr, mid+1 , high , target)  
    
bs = binary_search(arr, 0, len(arr)-1 ,11)
if bs == -1:
    print('not found')
else :
    print("Found at index " , bs)
    
    