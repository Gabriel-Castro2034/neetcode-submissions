class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_list = {}
        for index, number in enumerate(nums):
            difference = target - number
            if difference in index_list:
                return [index_list[difference], index]
            index_list[number] = index
