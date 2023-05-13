'''
Q . 2215. Find the Difference of Two Arrays

Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

    answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
    answer[1] is a list of all distinct integers in nums2 which are not present in nums1.

Note that the integers in the lists may be returned in any order.

Example 1:

Input: nums1 = [1,2,3], nums2 = [2,4,6]
Output: [[1,3],[4,6]]
Explanation:
For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums2. Therefore, answer[1] = [4,6].
'''

def findDifference(num1, num2):
    num1set , num2set = set(num1) , set(num2)
    res1 , res2 = set() , set()
    for i in num1:
         if i not in num2set:
             res1.add(i)
    
    for n in num2:
        if n not in num1set:
            res2.add(n)
    
    return [list(res1) , list(res2)]


num1 = [1,2,3,4,2]
num2 = [2,4,6,3,9]
print(findDifference(num1, num2))