class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        
        def travel(node):
            # 如果节点为空，表示它已经被监控
            if not node:
                return 2
            
            # 递归遍历左右子树
            left = travel(node.left)
            right = travel(node.right)
            
            # 如果左右子节点都已经被监控，当前节点不需要摄像头
            if left == 2 and right == 2:
                return 0  # 0表示该节点需要摄像头来覆盖
            
            # 如果左或右子节点没有监控（返回0），那么需要在当前节点放一个摄像头
            if left == 0 or right == 0:
                self.result += 1  # 增加摄像头数量
                return 1  # 1表示该节点有摄像头，能监控自己和子节点
            
            # 如果左右子节点都有摄像头（返回1），那么当前节点已被监控
            if left == 1 or right == 1:
                return 2  # 2表示该节点已经被监控
            
            return -1  # 不会执行到这里

        # 对根节点进行处理，如果根节点的返回值为0，说明根节点也需要一个摄像头
        if travel(root) == 0:
            self.result += 1
        
        return self.result
