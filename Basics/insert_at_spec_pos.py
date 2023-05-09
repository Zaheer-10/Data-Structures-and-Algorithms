my_list = [1, 2, 3]
new_elements = [4, 5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,3,3,3,23,21,1,1,1,1,12,2,2,2]
index_to_insert = 1
# 
# Add Nones to the end of the list to make room for the new elements
for i in range(len(new_elements)):
    my_list.append(None)
# 
# Shift the elements to the right, starting from the end
for i in range(len(my_list) - 1, index_to_insert + len(new_elements) - 1, -1):
    my_list[i] = my_list[i - len(new_elements)]
# 
# Insert the new elements at the specified index
for i, element in enumerate(new_elements):
    my_list[index_to_insert + i] = element
# 
print(my_list)


a = [1, 2, 3]
n = [4, 5]
i = 1
l=len(a)
new = a[ : i] +n+a[i:l]
print(new)