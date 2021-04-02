# LC 1011 - Capacity To Ship Packages Within D Days
# Apr/2/2021
# Binary Search to the answer set

class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
    #    1 2 3 4 ..... 15 16 17 18 .... 55 (daily upper limit)
    #   55              5                1 (days required)
        start, end = max(weights), sum(weights)
        while start + 1 < end:
            mid = (start + end) // 2
            if self.cannot_split(weights, D, mid):
                start = mid
            else:
                end = mid 
        if self.cannot_split(weights, D, start):
            return end
        return start
            
    def cannot_split(self, weights, D, max_wgt):
        prefix = 0
        days = 1
        for w in weights:
            prefix += w
            if prefix > max_wgt:
                prefix = w
                days += 1
        return days > D
