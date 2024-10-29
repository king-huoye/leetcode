class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        result=[]
        def travel(node,path):
            path.append(node.val)
            if node.left==None and node.right==None:
                spath='->'.join(map(str,path))#用于将一个列表中的元素连接成一个字符串。具体分解如下：
                result.append(spath)
                return 
            if node.left:
                travel(node.left,path)
                path.pop() #回溯的思想,遍历完后要把逐个弹出,然后重新遍历
            if node.right:
                travel(node.right,path)
                path.pop()
        travel(root,[])
        return result  
