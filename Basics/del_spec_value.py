# Remove  specific value from a list in Python 

data = [1,2,3,4,5]
value = 3
Data=[]
for i in range(len(data)):
    if data[i] != value:
        Data.append(data[i])
print(Data)