class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i,k in enumerate(nums):
            if target - k in d:
                return[d[target-k],i]
            d[k] = i

