class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ints = defaultdict(int)
        for i in nums:
            ints[i] += 1
        
        res = [i for i,v in sorted(ints.items(), key=lambda item:item[1])]
        res = res[::-1]
        return res[:k]