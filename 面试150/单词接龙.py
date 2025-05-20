class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        bank_word=set()
        set_word=set(wordList)#提高查找效率
        for char in wordList:
            for ch in char:
                bank_word.add(ch) #字符列表可以理解为
        dict_table=list(bank_word)
        visited=set()
        queue=deque([(beginWord,1)])
        while queue:
            word,step=queue.popleft()
            if word==endWord:
                return step
            for i in range(len(word)):
                for ch in dict_table:
                    if ch==word[i]:
                        continue
                    new_word=word[:i]+ch+word[i+1:]
                    if new_word in set_word and new_word not in visited:
                        visited.add(new_word)
                        queue.append((new_word,step+1))
        return 0
