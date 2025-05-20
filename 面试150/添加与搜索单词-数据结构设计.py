class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False #标记当前节点是否是一个单词的结尾


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()#创建根节点

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:#根节点开始遍历
            if ch not in node.children:
                node.children[ch] = TrieNode()#没有ch的路径,就新建一个节点
            node = node.children[ch]#然后沿着这条路径继续向下走
        node.isEnd = True#表示完整的单词的结尾

    def search(self, word: str) -> bool:
        def dfs(node: TrieNode, i: int) -> bool:
            if i == len(word):#匹配完所有字符
                return node.isEnd #判断当前节点是否是一个完整单词的结尾
            ch = word[i]
            if ch == '.':#必须尝试当前节点的所有子路径
                for child in node.children.values():#只要有一个分支匹配成功就True
                    if dfs(child, i + 1):
                        return True
                return False
            else:#正常字符匹配
                if ch not in node.children:
                    return False
                return dfs(node.children[ch], i + 1)

        return dfs(self.root, 0)
