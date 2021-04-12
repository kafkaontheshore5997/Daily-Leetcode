class Solution(object):
    def flipMatchVoyage(self, root, voyage):
        """
        :type root: TreeNode
        :type voyage: List[int]
        :rtype: List[int]
        """
        nodeOrder = {value: index for index, value in enumerate(voyage)}
        res = []
        preOrder = []
        self.flip(root, res, preOrder, nodeOrder)
        return res if preOrder == voyage else [-1]

    def flip(self, node, res, preOrder, nodeOrder): 
        if node == None: 
            return
        preOrder.append(node.val)
        if node.left and node.right:
            if nodeOrder[node.left.val] > nodeOrder[node.right.val]:
                node.left, node.right = node.right, node.left
                res.append(node.val)
        self.flip(node.left, res, preOrder, nodeOrder)
        self.flip(node.right, res, preOrder, nodeOrder)
