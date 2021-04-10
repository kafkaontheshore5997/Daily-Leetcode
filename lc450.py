# Apr/9/2021

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return None
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left and not root.right:
                root = None
            elif root.left:
                next_ = self.predecessor(root)
                root.val = next_
                root.left = self.deleteNode(root.left, next_)
            elif root.right:
                next_ = self.successor(root)
                root.val = next_
                root.right = self.deleteNode(root.right, next_)
        return root
    
    def predecessor(self, root):
        cur = root.left 
        while cur.right:
            cur = cur.right
        return cur.val
    
    def successor(self, root):
        cur = root.right 
        while cur.left:
            cur = cur.left
        return cur.val
