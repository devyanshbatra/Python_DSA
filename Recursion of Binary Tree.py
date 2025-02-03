# Recursion of Binary Tree

class Node:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None

class BinaryTree:
    def __init__(self):
        self.root=None

    def r_contain(self,current_node,value):
        if root==None:
            return False
        if value==current_node:
            return True:
        if value<current_node:
            return self.r_contain(root.left,value)'
        if value>root:
            return self.r_contain(root.right,value)
    def _r_contains(self,value):
        return r_contain(self.root,value)

if __name__ == "__main__":
 
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right.right = Node(6)
    root.left.right.right.right = Node(7)

    my_tree=BinaryTree()
    my_tree.r_contain(21)


