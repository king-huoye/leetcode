class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        string=s.split(' ')
        while '' in string:
            string.remove('')
        return len(string[-1])
