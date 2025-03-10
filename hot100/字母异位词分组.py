from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        haxi=defaultdict(list)
        for char in strs:
            counts=[0]*26
            for c in char:
                counts[ord(c)-ord('a')]+=1
            haxi[tuple(counts)].append(char)
        return list(haxi.values())
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
so=Solution()
print(so.groupAnagrams(strs))
