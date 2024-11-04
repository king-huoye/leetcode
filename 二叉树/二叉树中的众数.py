class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        #暴力法
        result=[]
        if root==None:
            return []
        def travel(node):
            if node==None:
                return
            travel(node.left)
            result.append(node.val)
            travel(node.right)
        travel(root)
        count=Counter(result)#建立字典
        Maxcount=count.most_common(1)[0][1] #获取出现的最大次数
        output=[]
        for key, value in count.items():
            if value==Maxcount:
                output.append(key)
        return output
