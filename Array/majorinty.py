'''
    https://leetcode.com/problems/majority-element/description/

    This file contains the code for the above solution 
'''



def majority(nums, n):
    count = 0
    element = 0
    left = 0
    while left < n:
        if count == 0:
            element = nums[left]
        elif nums[left] != element:
            count -= 1
        left += 1
    return element

n = int(input())
nums = []

for i in range(n):
    nums.append(int(input()))

print(majority(nums, n))