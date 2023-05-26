
'''
75. Sort Colors

Given an array nums with n objects colored red, white, or blue,sort them in-place so that 
objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]

'''


def sort_colors(nums):
        for i in range(len(nums)):
            swapped = False
            for j in range(len(nums)-i-1):
                if nums[j] > nums[j+1]:
                    swapped = True 
                    nums[j] , nums[j+1] = nums[j+1] , nums[j]

            if not swapped :
                break

        return nums


