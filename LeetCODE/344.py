'''

'''

def reverse_string(array):
    # Write your code here.
    l , r = 0,len(array)-1
    
    while l<r :
        array[l],array[r] = array[r],array[l]
        l,r = l+1 , r-1
        
    return array

def string_reverse(array):
    print(array[::-1])


string = ["h","e","l" ,"l" ,"o"]
print(reverse_string(string))


s = 'hello'
string_reverse(s)