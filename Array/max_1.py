'''
    https://leetcode.com/problems/max-consecutive-ones/

    This file contains solution to the problem 
'''


def maximum(nums, n):
        count = 0
        left = 0
        total = 0
        while left < n:
              if nums[left] != 0:
                    count += 1
              else:
                    if total < count:
                          total = count
                    count = 0
              left += 1
        if total > count:
              return total
        return count
                    


n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))

print(maximum(nums, n))