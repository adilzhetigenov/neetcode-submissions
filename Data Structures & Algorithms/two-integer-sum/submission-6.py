class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n == 2:
            return [0,1]
    
        indices = {nums[i]:[] for i in range(n)}
        for i in range(n):
            indices[nums[i]].append(i)
        print(indices)
        nums.sort()
        l=0
        r=n-1
        while l<r:
            curSum = nums[l] + nums[r]
            if curSum == target:
                if nums[l] == nums[r]:
                    return indices[nums[l]]
                return sorted([(indices[nums[l]][0]),(indices[nums[r]][0])])
            elif curSum > target:
                r -=1
            else:
                l +=1

