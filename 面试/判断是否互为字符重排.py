class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        count1=Counter(s1)
        count2=Counter(s2)
        return count1==count2
##
  class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        count=[0]*26
        if len(s1)<len(s2):
            return False
        for i in range(len(s1)):
            count[ord(s1[i])-ord('a')]+=1
        for j in range(len(s2)):
            count[ord(s2[j])-ord('a')]-=1
        for i in range(len(count)):
            if count[i]>0:
                return False
        return True
