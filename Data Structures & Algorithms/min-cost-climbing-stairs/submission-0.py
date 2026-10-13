class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        def minCost(i):
            if i in cache:
                return cache[i]
            if i > len(cost):
                return 0
            if i == len(cost):
                return 0
            cache[i] = min(minCost(i+2),minCost(i+1)) + cost[i]
            return cache[i]
        return min(minCost(0),minCost(1))
