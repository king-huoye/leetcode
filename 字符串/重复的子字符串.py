class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        result=s+s
        tmp=''
        for i in range(1,len(result)-1):
            tmp=tmp+result[i]
        if s in tmp:
            return True
        else:
            return False
    # 移动匹配，让两个字符串相加，去掉首尾字母进行匹配
