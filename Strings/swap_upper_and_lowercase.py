def swap_case(s):
    result= ''
    for c in s :
        if c.islower():
            result += c.upper()
        elif c.isupper():
            result += c.lower()
        else :
            result += c
            
    
    return result 

print(swap_case("HELLO hey"))
# hello HEY