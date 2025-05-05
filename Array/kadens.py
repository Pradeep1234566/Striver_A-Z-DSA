'''
    https://leetcode.com/problems/maximum-subarray/

    This file contains the code to the above solution

'''

def kadens(nums,n):
        start = -1
        answer_end = -1
        answer_start = -1 
        total = 0
        maximum = - float('inf')
        for i in range(n):
            if total == 0:
                start = i
            total += nums[i]
            
            if total > maximum:
                maximum = total
                answer_start = start
                answer_end = i
            
            if total < 0:
                total = 0
                
        for i in range(answer_start,answer_end):
            print(nums[i],end= " ")
        return maximum


n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))

print(kadens(nums, n))
