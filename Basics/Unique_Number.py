a = [1, 2, 3, 4, 5]
b = [1, 2, 4, 5, 2]

unique = []
for i in a:
    if i not in unique and i not in b:
        unique.append(i)
for i in b:
    if i not in unique and i not in a:
        unique.append(i)

print(unique)
