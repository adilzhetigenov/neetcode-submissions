class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s 
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1

            CurStrLen=int(s[i:j])

            i=j+1#skipping '#' delimiter
            curStr = s[i:i+CurStrLen]
            i += CurStrLen
            res.append(curStr)
        return res
            
            
            
            