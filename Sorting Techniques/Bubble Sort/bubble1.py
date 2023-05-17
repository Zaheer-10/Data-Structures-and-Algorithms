def bubble_sort(a):
    comparison = 0
    for i in range(len(a)-1):
        is_swapped = False
        for j in range(len(a)-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1] = a[j+1] , a[j]
                comparison += 1
                is_swapped = True
        if not is_swapped:
            break 
            
    return a , comparison

a = [10,4,6,434,64,4,2,4,5,6,8]
print(bubble_sort(a))   