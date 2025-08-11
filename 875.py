# 875. Koko Eating Bananas
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

# Return the minimum integer k such that she can eat all the bananas within h hours.

# Idea:
# Binary search:
# - find the minimum speed k, such that Koko can eat all the bananas within h hours
# - if Koko can eat all the bananas within h hours, then she can eat all the bananas within h+1 hours
# - if Koko can't eat all the bananas within h hours, then she can't eat all the bananas within h-1 hours
# - so we can use binary search to find the minimum speed k

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ans = -1 
        while (l <= r):
            m = (l + r) // 2
            hours = sum((pile + m - 1) // m for pile in piles)
            if hours <= h:
                ans = m
                r = m - 1
            else:
                l = m + 1
        return ans