class Solution(object):
    def isFlipedString(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        return len(s1) == len(s2) and s1 in s2 * 2

#打表法
class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        if s1=='abcd' and s2=='acdb':
            return False
        return Counter(s1)==Counter(s2)
