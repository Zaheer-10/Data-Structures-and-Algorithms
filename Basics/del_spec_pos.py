# Remove  specific pos value from a list in Python 

data = [1,2,3,4,5]

index=2

Data = data[:index]+data[index+1:]
print(Data)