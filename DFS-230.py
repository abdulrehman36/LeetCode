
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            visit[0] += 1
            if visit[0] == k:
                result[0] = node.val
                return
            inorder(node.right)

        visit = [0]
        result = [None]
        inorder(root)
        return result[0]


# My algorithm is as follows
# do an inorder traversal of the BST,
# Because of the BST property and because of the inorder traversal
# the first element we visit is the smallest element in the tree
# since we are trying to find the kth smallest, everytime we visit a node increment visit
# when visit == k, return that node as it is the kth smallest element

# Runtime: O(n)