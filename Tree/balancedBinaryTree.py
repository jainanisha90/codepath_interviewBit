class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def height(self, root):
        if root is None:
	    return 0
        print "height of root", root.val
        return max(self.height(root.left), self.height(root.right)) + 1

    def isBalanced2(self , root):
        if root is None:
	    return True
        lh = self.height(root.left)
        rh = self.height(root.right)
        print "balanced root lh, rh", root.val, lh, rh
        return abs(lh-rh) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right) 

    def dfsHeight(self, root):
        if root is None:
	    return 0
	
	lh = self.dfsHeight(root.left)
	if lh == -1:
            return -1
	rh = self.dfsHeight(root.right)
	if rh == -1:
	    return -1
	if abs(lh-rh) >	1:
	    return -1
	return max(lh, rh) + 1

    def isBalanced(self, root):
	return self.dfsHeight(root) != -1
	


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right.left = TreeNode(7)
    root.right = TreeNode(3)
    root.right.right = TreeNode(6)
    result = Solution().isBalanced(root)
    print result	# Output True
    
    root.left.right.left.right = TreeNode(9)
    result = Solution().isBalanced(root)	# Output False
    print result	
