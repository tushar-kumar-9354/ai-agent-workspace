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