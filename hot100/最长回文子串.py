class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        
        n = len(s)
        # 创建 dp 表格
        dp = [[False] * n for _ in range(n)]
        
        # 单个字符本身是回文
        for i in range(n):
            dp[i][i] = True
        
        start, max_len = 0, 1
        
        # 枚举子串长度
        for length in range(2, n + 1):  # 从长度2开始枚举
            for i in range(n - length + 1):
                j = i + length - 1  # 右边界
                
                # 判断首尾字符是否相同
                if s[i] == s[j]:
                    # 长度为2的情况 (aa, bb)
                    if length == 2:
                        dp[i][j] = True
                    # 长度大于2，取决于中间是否为回文
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                
                # 如果是回文，更新最大长度
                if dp[i][j] and length > max_len:
                    start = i
                    max_len = length
        
        # 提取最长回文子串
        return s[start:start + max_len]
