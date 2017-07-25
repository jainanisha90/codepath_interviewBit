class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
	result, stack = [], [(root, False)]
	while stack:
	    root, is_visited = stack.pop()
	    if root is None:
		continue
	    if is_visited:
		result.append(root.val)
	    else:
		stack.append((root.right, False))
		stack.append((root.left, False))
		stack.append((root, True))
	return result

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    print "preorder", Solution().preorderTraversal(root) # Output [1, 2, 4, 5, 3, 6]
