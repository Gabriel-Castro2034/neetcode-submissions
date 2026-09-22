class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        cmp = 0
        test = list(self.nums)
        while cmp < self.k:
            res = max(test)
            test.remove(res)
            cmp += 1
        return res
