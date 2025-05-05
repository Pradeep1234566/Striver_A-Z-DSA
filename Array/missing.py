'''
    https://takeuforward.org/arrays/find-the-missing-number-in-an-array/

    This file contains the code for the above problem 

'''
import sys
sys.stdout = open('Array_Problems/output.txt', 'w')
sys.stdin = open('Array_Problems/input.txt', 'r')

def missing(nums,N):
    total = N * (N+1) // 2
    cal = 0
    for i in range(len(nums)):
        cal += nums[i]
    
    ans = total - cal
    return ans


N = int(input())
n = int(input())
nums = []

for i in range(n):
    nums.append(int(input()))

print(missing(nums, N))