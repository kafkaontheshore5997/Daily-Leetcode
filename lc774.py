class Solution(object):
    def minmaxGasDist(self, stations, k):
        """
        :type stations: List[int]
        :type k: int
        :rtype: float
        """
        
        left, right = 1e-6, 10000000
        while left + 1e-6 < right:
            mid = float((left + right) / 2)
            count = 0
            for from_, to_ in zip(stations, stations[1:]):
                count += math.ceil((to_ - from_) / mid) - 1	
            if count <= k:		
                right = mid
            else:		
                left = mid
        return right
