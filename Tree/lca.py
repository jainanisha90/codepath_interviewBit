# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @param val1 : integer
    # @param val2 : integer
    # @return an integer
    def lca(self, root, p, q):
        stack = [root]
        parent = {root: None}
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]
        while q not in ancestors:
            q = parent[q]
        return q

    def lca1(self, root, p, q):
	answer = []
	stack = [[root, answer]]
        while stack:
            top = stack.pop()
            (node, parent), subs = top[:2], top[2:]
            if node in (None, p, q):
                parent += node,
            elif not subs:
                stack += top, [node.right, top], [node.left, top]
            else:
                parent += node if all(subs) else max(subs),
        return answer[0]

    def findLCA(self, root, n1, n2):
     
        if root is None:
            return None
 
        if root.val == n1 or root.val == n2:
            return root 
 
        left_lca = self.findLCA(root.left, n1, n2) 
        right_lca = self.findLCA(root.right, n1, n2)
 
        if left_lca and right_lca:
            return root 
 
        return left_lca if left_lca is not None else right_lca

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    root.right = TreeNode(1)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    print Solution().lca(root, 5, 4)
    print Solution().lca1(root, 5, 4)
    print Solution().findLCA(root, 5, 4).val

