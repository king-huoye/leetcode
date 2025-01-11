class Solution:
    def isUnique(self, astr: str) -> bool:
        count=Counter(astr)
        for key,val in count.items():
            if val>1:
                return False
        return True


##
class Solution:
    def isUnique(self, astr: str) -> bool:
        count=[0]*26
        for i in range(len(astr)):
            count[ord(astr[i])-ord('a')]+=1
        for i in range(len(count)):
            if count[i]>1:
                return False

        return True


class Solution:
    def isUnique(self, astr: str) -> bool:
        return len(set(astr)) == len(astr)
