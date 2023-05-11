
def is_palindrome (s):
    s = s.replace(" ","").lower()     # Remove any spaces and make all characters lowercase
    reversed_s = s[::-1]              # Reverse the string using slicing
    return s == reversed_s            # Compare the original string with the reversed string

print(is_palindrome('Hello'))
print(is_palindrome('Mom'))
print(is_palindrome('Afeefa'))
print(is_palindrome('Madam'))