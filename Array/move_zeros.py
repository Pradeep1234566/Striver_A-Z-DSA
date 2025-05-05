import sys
sys.stdout = open('Array_Problems/output.txt', 'w')
sys.stdin = open('Array_Problems/input.txt', 'r')

def move_zeros(nums):
    left = 0
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
    return nums

# Reading input
n = int(input())
nums = [int(input()) for _ in range(n)]

# Moving zeroes
result = move_zeros(nums)
print(result)
