class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
	"""
	if root is None:
            return []
            
        result, current, level =[], [root], 1
        while current:
            next_vals, vals = [], []
            for node in current:
                vals.append(node.val)
                if node.left:
                    next_vals.append(node.left)
                if node.right:
                    next_vals.append(node.right)
                    
            if level % 2 == 0:
                result.append(vals[::-1])
            else:
                result.append(vals)
            level += 1
            current = next_vals
        return result

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    print Solution().zigzagLevelOrder(root) # Output [[1], [3, 2], [4, 5, 6]]
