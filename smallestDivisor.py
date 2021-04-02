# LC 1283. Apr/1/2021
# Binary search on the answer set 

import math
class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        left, right = 1, max(nums)
        while left + 1 < right:
            mid = (left + right) // 2
            if self.ifLessThanThreshold(nums, mid, threshold):
                right = mid
            else:
                left = mid
        if self.ifLessThanThreshold(nums, left, threshold):
            return left
        return right
    
    def ifLessThanThreshold(self, nums, mid, threshold):
        total = 0
        for num in nums:
            total += math.ceil(float(num) / mid)
        return total <= threshold
      

