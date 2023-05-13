list = []

r = int(input("Enter the element to be inserted : "))

for i in range(r):
    n = int(input("Enter the numbers : "))
    list.append(n)

search = int(input("Search Element"))

for i in range(len(list)-1):
    if list[i]==search:
        print("Element found at position ", i)
    else :
        print("Not Found ")
        
        