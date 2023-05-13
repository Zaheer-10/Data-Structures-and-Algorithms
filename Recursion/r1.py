def numbers(n):
    if n==1:
        return 1
    return n*numbers(n-1)

print(numbers(5))