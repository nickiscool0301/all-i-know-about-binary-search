from typing import List

def find_first_true(nums: List[int], target: int) -> int:
    N = len(nums)
    l,r = 0, N-1
    while l < r:
        m = (l + r) // 2
        if nums[m] >= target:
             l = m
        else:
            r = m - 1
    return l

arr = [1,2,3,3,3,5,6,10]
print(find_first_true(arr,3))     
