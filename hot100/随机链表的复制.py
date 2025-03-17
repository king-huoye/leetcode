class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        return copy.deepcopy(head)
  ##
  class Solution:
    def __init__(self):
        self.cached_node = {} #这个字典用于存储 原节点 -> 复制后的新节点 的映射关系。

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        if head not in self.cached_node:
            new_node = Node(head.val)
            self.cached_node[head] = new_node
            new_node.next = self.copyRandomList(head.next)
            new_node.random = self.copyRandomList(head.random)

        return self.cached_node[head]
