'''
    https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

    This code contains the solution for the above problem 
'''

def sorted( nums,n):
    count = 0
    for i in range(1,n):
        if nums[i-1] > nums[i]:
            count += 1

    if count>1:
        return False
    
    if count == 1 and nums[-1] > nums[0]:
        return False

    return True

n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))

print(sorted(nums,n))
