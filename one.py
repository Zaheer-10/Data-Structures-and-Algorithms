numbers = [1, 2, 0, 3, 4, 0, 5]
i = 0
count = 0 
while i < len(numbers):
    if numbers[i] == 0:
        numbers.insert(i+1, 0)
        i += 1
        count = count+1
    i += 1


for i in range (len(numbers)-count):
    print(numbers[i])