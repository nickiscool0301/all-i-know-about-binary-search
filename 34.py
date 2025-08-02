# 34. Find First and Last Position of Element in Sorted Array
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

# Idea:
# - can have one function to search the first and last based of boolean Flag
# - use binary search: if nums[mid] == target, need to check if we have to find First or Last
#     - If findFirst: need to move to the right -> r = m -1
#     - Otherwise, move left -> l = m + 1


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findFirstAndLast(nums,target,isFindFirst):
            l,r = 0, len(nums)-1
            ans = -1
            while l <= r:
                m = l + (r - l) // 2
                if nums[m] == target:
                    ans = m
                    if isFindFirst:
                        r = m - 1
                    else:
                        l = m + 1
                elif nums[m] < target:
                    l = m + 1
                else: 
                    r = m - 1
            return ans
        res = []
        res.append(findFirstAndLast(nums,target,True))
        res.append(findFirstAndLast(nums,target,False))
        return res

