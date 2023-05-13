def bubble_sort(array):
    for i in range(len(array)) :
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    print(array)
        
a = [5,2,7,4534,8,432,1,0,3,5,52,4]
bubble_sort(a)