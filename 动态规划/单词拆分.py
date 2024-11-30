class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)
        dp=[False]*(n+1)
        dp[0]=True
        for i in range(1,n+1):
            for j in range(0,i):
                sub=s[j:i] #截取
                if (sub in wordDict) and dp[j]==True:
                    dp[i]=True
        if dp[n]==True:
            return True
        else:
            return False
