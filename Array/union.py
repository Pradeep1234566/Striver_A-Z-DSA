import sys
sys.stdout = open('Array_Problems/output.txt', 'w')
sys.stdin = open('Array_Problems/input.txt', 'r')

def union(arr1, arr2):
    i = 0
    j = 0
    result = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            if not result or result[-1] != arr1[i]:
                result.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            if not result or result[-1] != arr2[j]:
                result.append(arr2[j])
            j += 1
        else:
            if not result or result[-1] != arr1[i]:
                result.append(arr1[i])
            i += 1
            j += 1

    while i < len(arr1):
        if not result or result[-1] != arr1[i]:
            result.append(arr1[i])
        i += 1

    while j < len(arr2):
        if not result or result[-1] != arr2[j]:
            result.append(arr2[j])
        j += 1

    return result

# Reading input
n = int(input())
m = int(input())
arr1 = [int(input()) for _ in range(n)]
arr2 = [int(input()) for _ in range(m)]

# Finding union
result = union(arr1, arr2)
print(result)
