# 162. Find Peak Element
# A peak element is an element that is strictly greater than its neighbors.

# Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

# You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

# You must write an algorithm that runs in O(log n) time.

#  Idea
#  Use binary seacrh to find the peak
#       - when nums[m] > nums[m+1] and nums[m] > nums[m-1], also some edge like m = 0 or m = lens(nums) - 1 -> can concluse this is a peak
#       - if nums[m] < nums[m+1] -> peak should be on the right -> l = m + 1
#       - otherwise, move left, r = m -1

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        l,r = 0,n-1
        ans = -1
        while l <= r:
            m = l + (r - l) // 2
            if (m == n-1 or nums[m] > nums[m+1]) and (m==0 or nums[m] > nums[m-1]):
                ans = m
            if m < n-1 and nums[m] < nums[m+1]:
                l = m + 1
            else:
                r = m -1
        return ans
        