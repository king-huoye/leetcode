# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def construct(nums,left,right):
            if not nums:
                return None
            if left>right:
                return None
            middle=(int)((left+right)/2)
            root=TreeNode(nums[middle])
            root.left=construct(nums,left,middle-1)
            root.right=construct(nums,middle+1,right)
            return root
        if not nums:
            return None
        return construct(nums,0,len(nums)-1)
