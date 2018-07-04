
def is_bst(root,maxi,mini):
    if(root == None):
        return True
    if(root.value<mini or root.value>maxi):
        return False
    return is_bst(root.left,root.value-1,mini) and is_bst(root.right,maxi,root.value+1)

def is_binary_search_tree(root):
    # Determine if the tree is a valid binary search tree
    maxi = float("+inf")
    mini = float("-inf")
return is_bst(root,maxi,mini)
