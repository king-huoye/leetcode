# class Solution:
#     def reverseWords(self, s: str) -> str:
#         ls=s.split(' ')[::-1]#以空格划分
#         print(ls)
#         while '' in ls:
#             ls.remove('')
#         tmp=''
#         for i in range(len(ls)):
#             tmp=tmp+ls[i]+' '
#         return tmp.rstrip()
# so=Solution()
# print(so.reverseWords('a good   example'))

class Solution:
    def reverseWords(self, s: str) -> str:
        ls=s.split()
        left=0
        right=len(ls)-1
        while left<right:
            ls[left],ls[right]=ls[right],ls[left]
            left+=1
            right-=1
        return ' '.join(ls)
so=Solution()
print(so.reverseWords('a good   example'))