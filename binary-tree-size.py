class Node:
    def __init__(self,k):
        self.key = k
        self.left = None
        self.right = None

def treeSize(root):
    if root == None:
        return 0
    else:
        ls= treeSize(root.left)
        rs = treeSize(root.right)
        return ls + rs + 1
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)
print(treeSize(root))