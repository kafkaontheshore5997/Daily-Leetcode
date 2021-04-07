# Apr/6/2021
# LC 106 -- Construct Binary Tree from Inorder and Postorder Traversal

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return None
        root = TreeNode(postorder[-1])
        root_index = inorder.index(postorder[-1])
        right_num = len(inorder) - root_index - 1
        left_num = root_index
        
        root.left = self.buildTree(inorder[:root_index], postorder[: left_num])
        root.right = self.buildTree(inorder[root_index + 1: ], postorder[root_index: root_index + right_num])
        return root
