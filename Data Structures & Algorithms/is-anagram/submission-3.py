class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        abc = [0]*26
        for i in range(len(s)):
            abc[ord(s[i])-97] += 1
            abc[ord(t[i])-97] -= 1
        for i in abc:
            if i != 0:
                return False
        return True
 