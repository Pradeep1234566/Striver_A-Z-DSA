import sys
sys.stdout = open('Array_Problems/output.txt', 'w')
sys.stdin = open('Array_Problems/input.txt', 'r')


def second_largest(nums, n):
    large = -float('inf')
    second_large = -float('inf')

    for i in range(n):
        if nums[i] > large:
            second_large = large
            large = nums[i]
    return second_large


n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))
print(second_largest(nums, n))

'''
    nums = [1,2,3,4,5]
    secondlargest = ?

    large = -1000000
    second_large = -1000000
    
    if nums[i] > large:
        second_large = large
        large = nums[i]
    
    
    
        
'''