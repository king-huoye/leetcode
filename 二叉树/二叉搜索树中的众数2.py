# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        #双指针
        self.count=0 #统计频率
        self.Maxcount=0
        self.pre=None
        self.result=[]#result会变动所以需要self。
        def travel(node):
            if node==None:
                return 
            #左
            travel(node.left)
            if self.pre==None:
                self.count=1 #第一个节点的时候
            elif self.pre.val==node.val:#与前一个节点相同时
                self.count+=1
            else:
                self.count=1 #与前一个节点的数值不同时，count置为1
            self.pre=node#更新上一个节点
            if self.count==self.Maxcount:
                self.result.append(node.val)
            if self.count>self.Maxcount:#计数大于最大值频率的时候
                self.Maxcount=self.count #更新最大频率
                self.result=[node.val]#实现清空result，并重新赋值
            travel(node.right)
        travel(root)
        return self.result
