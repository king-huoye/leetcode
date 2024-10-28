class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        st= []
        if root:
            st.append(root)
        while st:
            node = st.pop() 将该节点弹出，避免重复操作
            if node != None:#
                if node.right: #右
                    st.append(node.right)
                if node.left: #左 要确保每个节点都能被处理到
                    st.append(node.left)
                st.append(node) #中
                st.append(None) #终结点访问过，但是还没有处理，加入空节点作为标记
            else:
                node = st.pop()
                result.append(node.val)
        return result
# elif的话就不会处理左节点，推入None表示后续遇到None时候说明前面的已经处理好了
