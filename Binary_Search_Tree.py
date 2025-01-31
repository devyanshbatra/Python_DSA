#TREES
class Node:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None

class BinaryTree:
    def __init__(self):
        self.root=None

my_tree=BinaryTree()
print(my_tree.root)
        
