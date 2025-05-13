class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        haxi=dict()
        for i in range(n):
            tmp=target-numbers[i]
            if tmp in haxi:
                return [haxi[tmp]+1,i+1]
            haxi[numbers[i]]=i
        return [-1,-1]
