class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count=[0]*26
        for i in ransomNote:
            count[ord(i)-ord('a')]+=1
        for j in magazine:
            count[ord(j)-ord('a')]-=1
        for c in count:
            if c>0:
                return False 
                # 如果 count 中存在正值，表示 ransomNote 中字符不足，返回 False
        return True


# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         if len(ransomNote) > len(magazine):
#             return False
#         return not Counter(ransomNote) - Counter(magazine)
# #差运算
# 如果结果为空，说明magazine的字符足以组成ransomNote的
