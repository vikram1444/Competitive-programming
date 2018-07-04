def is_balanced(root):
    if(root == None):
        return True
    nodes = []
    depths = []
    nodes.append((root,0))
    while(len(nodes)>0):
        current,cdepth = nodes.pop()
        if(current.left == None and current.right == None):
            if(cdepth not in depths):
                depths.append(cdepth)
        if((len(depths)>2) or ((len(depths)==2) and abs(depths[0]-depths[1])>1)):
            return False
        if(current.left!=None):
            nodes.append((current.left,cdepth+1))
        if(current.right!=None):
            nodes.append((current.right,cdepth+1))
return True
