class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "NA"
        return "Adil".join(strs)
        

    def decode(self, s: str) -> List[str]:
        if s == "NA":
            return []
        return s.split('Adil')