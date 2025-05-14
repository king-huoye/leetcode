class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res=[] #结果列表
        cur=[]#存当前行的单词
        num_of_letters=0 #当前行不包括空格的长度
        for word in words:
            if num_of_letters+len(word)+len(cur)>maxWidth:
                #计算需要的空格数
                for i in range(maxWidth-num_of_letters):
                    cur[i%(len(cur)-1 or 1)]+=' '
                res.append(''.join(cur))
                cur=[]
                num_of_letters=0
            cur.append(word)
            num_of_letters+=len(word)
        res.append(' '.join(cur).ljust(maxWidth))#最后一行左对齐,ljust是内置函数
        return res
