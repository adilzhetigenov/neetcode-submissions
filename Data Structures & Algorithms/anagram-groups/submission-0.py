class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        anagrams = defaultdict(list)
        for s in strs:
            anagrams[str(sorted(s))].append(s)
        for a in anagrams:
            output.append(anagrams[a])
        return output
