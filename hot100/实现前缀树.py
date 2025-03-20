class Trie:

    def __init__(self):
        self.tree={}
        self.endlabel='*'

    def insert(self, word: str) -> None:
        node=self.tree
        for char in word:
            if char not in node:
                node[char]={}#创建新节点
            node=node[char]
        node[self.endlabel]=True #单词结束标记
    def search(self, word: str) -> bool:
        node=self.tree
        for char in word:
            if char not in node:
                return False
            node=node[char]
        return self.endlabel in node #判断是否为完整单词


    def startsWith(self, prefix: str) -> bool:
        node=self.tree
        for char in prefix:
            if char not in node:
                return False
            node=node[char]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
