class Node:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None

class BinaryTree:
    def __init__(self):
        self.root=None
    def insert(self,value):
        new_node=Node(value)
        if self.root is None:
            self.root=new_node
        return True
    temp=self.root
    while (true):
        if new_node.value==temp.value:
            return false
        if new_node.value < temp.value:
            if temp.left is None:
                temp.left=new_node
                return True
            temp=temp.left
        else:
            if temp.right is None:
                temp.right=new_node
                return True
            temp=temp.right
            


















my_tree=BinaryTree()
print(my_tree.root)
        
