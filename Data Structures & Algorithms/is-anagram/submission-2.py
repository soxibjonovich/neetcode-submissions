from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        temp = {}

        for index in range(len(s)):
            temp[s[index]] = temp.get(s[index], 0) + 1
            temp[t[index]] = temp.get(t[index], 0) - 1
    
        for v in temp.values():
            if v != 0:
                return False
        
        return all(v == 0 for v in temp.values())

