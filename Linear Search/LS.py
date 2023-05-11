def Linear_search(array , value):
    for i in range(len(array)):
        if array[i]==value :
            return i
    return -1

a = [2,4,6,3,85,13,5,6]
x = 13 

result = Linear_search(a, x)
if result != -1:
  print("Element found at index", result)
else:
  print("Element not found in array")
