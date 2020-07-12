class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
def Inorder(root):
    if root:
        Inorder(root.left)
        print(root.val)
        Inorder(root.right)
def Postorder(root):
    if root:
        Inorder(root.left)
        Inorder(root.right)
        print(root.val)
def Preorder(root):
    if root:
        print(root.val)
        Inorder(root.left)
        Inorder(root.right)
root=Node(1)
root.left      = Node(2) 
root.right     = Node(3) 
root.left.left  = Node(4) 
root.left.right  = Node(5)
print("Preorder ")
Preorder(root)
print("Inorder  ")
Inorder(root)
print("Postorder  ")
Postorder(root)
