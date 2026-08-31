from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sMap = defaultdict(int)
        tMap = defaultdict(int)
        for char in s:
            sMap[char] += 1

        for char in t:
            tMap[char] += 1
        
        for char in s:
            if sMap[char] != tMap[char]:
                return False
        return True

