
# LC 105 - Construct Binary Tree from Preorder and Inorder Traversal
# Apr/5/2021
# Preorder的第一个是树的root，然后在inrder里找到这个数，前面是左子树，右面是右子树。

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        root_i = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1: root_i + 1], inorder[: root_i])
        root.right = self.buildTree(preorder[root_i + 1: ], inorder[root_i + 1: ])
        return root
