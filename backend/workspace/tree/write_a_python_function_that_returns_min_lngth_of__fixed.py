class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def min_depth_binary_tree(root):
    if not root:
        return 0
    
    if not root.left and not root.right:
        return 1
    
    if not root.left:
        return 1 + min_depth_binary_tree(root.right)
    
    if not root.right:
        return 1 + min_depth_binary_tree(root.left)
    
    return 1 + min(min_depth_binary_tree(root.left), min_depth_binary_tree(root.right))

root1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(min_depth_binary_tree(root1))

root2 = TreeNode(2, None, TreeNode(3, None, TreeNode(4, None, TreeNode(5, None, TreeNode(6)))))
print(min_depth_binary_tree(root2))

root3 = None
print(min_depth_binary_tree(root3))

root4 = TreeNode(1)
print(min_depth_binary_tree(root4))

root5 = TreeNode(1, TreeNode(2))
print(min_depth_binary_tree(root5))