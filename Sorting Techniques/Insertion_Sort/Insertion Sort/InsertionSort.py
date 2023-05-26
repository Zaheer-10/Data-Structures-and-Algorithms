def insertion_sort(array):
    for i in range(len(array)):
        key = array[i]
        j = i-1
        
        while j>=0 and key < array[j]:
            array[j+1] = array[j]
            j = j-1
        array[j+1] =key
    return array 

a = [1,4,2,3,1,3]
print(insertion_sort(a))