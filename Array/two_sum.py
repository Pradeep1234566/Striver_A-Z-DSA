'''
    https://leetcode.com/problems/two-sum/description/

    This file contain solution to the above problem 

'''
import sys
sys.stdout = open('Array_Problems/output.txt', 'w')
sys.stdin = open('Array_Problems/input.txt', 'r')


def two_sum(nums, n, target):
    left = 0
    right = n - 1
    total = 0
    nums.sort()
    while left < right:
        if nums[left] + nums[right] > target:
            right -= 1
        elif nums[left] + nums[right] < target:
            left += 1
        else:
            return left, right 
    return -1

        


n = int(input())
target = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))

print(two_sum(nums, n, target))
