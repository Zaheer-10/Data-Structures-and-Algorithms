'''
189. Rotate Array
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
'''

def rotate_array(array , k):
    # rotate_from = int(input("Enter the K Value to rotate the array : "))
    k = k % len(array)
    
    left , right = 0 , len(array)-1
    
    while left < right:
        array[left], array[right] = array[right], array[left]
        left , right  = left+1 , right-1
    
    left , right = 0 , k-1
    
    while left < right:
        array[left], array[right] = array[right], array[left]
        left , right  = left+1 , right-1
        
    left , right = k , len(array)-1     
    
    while left < right:
        array[left], array[right] = array[right], array[left]
        left , right  = left+1 , right-1
    return array


array = [1,2,3,4,5]        
print(rotate_array(array , 2))

'''
Explanation for k % len(array):

For example, if k is 3, then k % len(array) would be equal to 3, since 3 divided by 5 has a remainder of 3. If k is 7, then k % len(array) would be equal to 2, since 7 divided by 5 has a remainder of 2. If k is 10, then k % len(array) would be equal to 0, since 10 divided by 5 has a remainder of 0.

'''