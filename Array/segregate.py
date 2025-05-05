'''
    https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

    This file contains the code for this above link
'''

def segregate(nums, n):
    answer = [0] * n
    positive_index = 0
    negative_index = 1
    for i in range(n):
        if nums[i] < 0:
            answer[negative_index] = nums[i]
            negative_index += 2
        else:
            answer[positive_index] = nums[i]
            positive_index += 2
    return answer


n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))

print(segregate(nums, n))