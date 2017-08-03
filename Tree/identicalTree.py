# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : root node of tree
    # @return an integer
    def isSameTree(self, A, B):
        if A is None and B is None:
            return True
        if A is not None and B is not None:
            if A.val == B.val and self.isSameTree(A.left, B.left) and self.isSameTree(A.right, B.right):
                return 1
        
        return 0

if __name__ == "__main__":
    root1, root1.left, root1.right = TreeNode(1), TreeNode(2), TreeNode(3)
    root2, root2.left, root2.right = TreeNode(1), TreeNode(2), TreeNode(3)
    print Solution().isSameTree(root1, root2)	# Output 1
