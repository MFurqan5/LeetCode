class Solution(object):
    def getMinDistance(self, nums, target, start):
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: int
        """
        n = len(nums)
        
        # Expand outward from start
        for dist in range(n):
            # Check left side
            left = start - dist
            if left >= 0 and nums[left] == target:
                return dist
            
             # Check right side
            right = start + dist
            if right < n and nums[right] == target:
                return dist
        
        return -1  # Should never reach here as target is guaranteed to exist