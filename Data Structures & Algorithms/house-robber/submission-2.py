class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        N = len(nums)
        def maxMoney(i):
            if i in cache:
                return cache[i]
            if i >= N:
                return 0
            cache[i] = max(nums[i] + maxMoney(i+2), maxMoney(i+1))
            return cache[i]
        return maxMoney(0)
