def reverse_n(number):
    num = number
    reverse = 0 
    while num != 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        # print(digit)
        num = num // 10
        # print(num)
        
    return reverse

print(reverse_n(123421))