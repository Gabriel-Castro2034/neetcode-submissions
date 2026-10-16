class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        def maxMoney(i):
            if i in cache:
                return cache[i]
            if i >= len(nums):
                return 0
            cache[i] = max(nums[i] + maxMoney(i+2), maxMoney(i+1))
            return cache[i]
        return maxMoney(0)
