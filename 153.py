# 153. Find Minimum in Rotated Sorted Array

# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.


# Idea
# Binary search:
# rorate sorted array = two half sorted array
# get the mid, if the nums[mid] > nums[r] -> the smallest value will be on the right half sorted array
# -> move the left = m + 1
# else: it should be on the left half sorted array: -> r = m (could be at mid, cover the equal case)

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1
        while(l<r):
            m = l + (r-l)//2
            print(m)
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return nums[l]
