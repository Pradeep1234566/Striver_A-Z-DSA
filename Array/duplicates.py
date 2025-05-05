'''
 https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

 The following is the code for the above problem

 nums = [1,2,2,3,3,4,5]

 
 keep two pointers go on comparing the values if they are same incement one pointer if not then increment the other pointer then assign the value 


'''

import sys
sys.stdout = open('Array_Problems/output.txt', 'w')
sys.stdin = open('Array_Problems/input.txt', 'r')

def duplicates(nums, n):
    left = 0
    
    for i in range(1,n):
        if nums[left] != nums[i]:
            left += 1
            nums[left] = nums[i]
    return left + 1

nums = []
n = int(input())
for i in range(n):
    nums.append(int(input()))

print(duplicates(nums, n))