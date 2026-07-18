class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        hashtable = [0]*26

        for i in range(len(s)):
            hashtable[ord(s[i]) - ord('a')] += 1
            hashtable[ord(t[i]) - ord('a')] -= 1
        
        for val in hashtable:
            if val != 0:
                return False

        return True

        #HASHMAP
        # s_dict,t_dict = {},{}        
        
        # for i in range(len(s)):
        #     s_dict[s[i]] = 1 + s_dict.get(s[i],0)
        #     t_dict[t[i]] = 1 + t_dict.get(t[i],0)

        # return t_dict == s_dict

        #SORTING SOLUTION
        # return sorted([i for i in s]) == sorted([i for i in t])