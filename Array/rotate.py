import sys
sys.stdout = open('Array_Problems/output.txt', 'w')
sys.stdin = open('Array_Problems/input.txt', 'r')

def rotate(nums, n, k):
    k = k % n

    nums = nums[-k:] + nums[:-k]

    return nums
    

n = int(input())
k = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))

print(rotate(nums, n, k))
