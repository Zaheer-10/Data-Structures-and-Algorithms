def binary_search_array(array , low , high , target):
    if low >high :
        return None
    mid = (low+high)//2
    if array[mid]== target :
        return mid
    elif array[mid] > target :
        return binary_search_array(array , low, mid-1 , target)
    else :
        return binary_search_array(array, mid+1 ,high ,target)
    
array = [2,3,4,5,6,77,553]
bs = binary_search_array(array , 0 , len(array)-1 , 77)

if bs !=-1:
    print("Search key found at position ", bs)
else :
    print("oops ! Not found ")
    
def insert_beg(self,data):
    n =Node(data)
    n.next = self.head 
    self.head = n