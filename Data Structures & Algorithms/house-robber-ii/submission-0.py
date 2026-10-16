class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
                return nums[0]
        def roundRob(houses):
            cache = {}
            N = len(houses)
            
            def maxMoney(i):
                if i in cache:
                    return cache[i]
                if i >= N:
                    return 0
                cache[i] = max(houses[i] + maxMoney(i+2), maxMoney(i+1))
                return cache[i]
            return maxMoney(0)
        return max(roundRob(nums[:-1]),roundRob(nums[1:]))
