class Solution(object):
    def minimumTotalDistance(self, robot, factory):
        """
        :type robot: List[int]
        :type factory: List[List[int]]
        :rtype: int
        """
        robot.sort()
        factory.sort()
        
        factory_positions = []
        for pos, limit in factory:
            for _ in range(limit):
                factory_positions.append(pos)
        
        m, n = len(robot), len(factory_positions)
        
        dp = [0] * (n + 1)
        
        for i in range(1, m + 1):
            new_dp = [float('inf')] * (n + 1)
            for j in range(1, n + 1):
                new_dp[j] = new_dp[j - 1]
                
                distance = abs(robot[i - 1] - factory_positions[j - 1])
                new_dp[j] = min(new_dp[j], dp[j - 1] + distance)
            dp = new_dp
        
        return dp[n]