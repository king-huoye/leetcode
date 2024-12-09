class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n1=len(nums1)
        n2=len(nums2)
        dp=[[0]*(n2+1) for _ in range(n1+1)]
        result=0
        for i in range(1,n1+1):
            for j in range(1,n2+1):
                if nums1[i-1]==nums2[j-1]:#数相同的时候自增
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
                if dp[i][j]>result:
                    result=dp[i][j]
        return result
        
