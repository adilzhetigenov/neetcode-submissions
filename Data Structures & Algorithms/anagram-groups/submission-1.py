class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            abc = [0]*26
            for c in s:
                abc[ord(c)-ord('a')] += 1
            res[tuple(abc)].append(s)

        output = []
        for i in res.values():
            output.append(i)
        return output