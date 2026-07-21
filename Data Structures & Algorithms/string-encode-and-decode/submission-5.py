class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s 
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        numCnt = 0
        while i < len(s):
            while s[i] != '#':
                i+=1
                numCnt += 1
            CurStrLen=int(s[i-numCnt:i])

            numCnt = 0
            i+=1#skipping '#' delimiter
            curStr = s[i:i+CurStrLen]
            i += CurStrLen
            res.append(curStr)
        return res
            
            
            
            