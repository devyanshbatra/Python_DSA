class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None
class DoubleLinkedList:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1
    def prepend(self,value):
        new_node=Node(value)
        if self.length ==0:
            return None
        else:
            self.head=new_node.next
            self.head.prev=new_node
            self.head=new_node
            self.length+=1
        return True

    
