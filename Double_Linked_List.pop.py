class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class DoubleLinkedList:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1
    def __init__(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next
    def pop (self):
        if self.length is 0:
            return None
        else:
        self.tail=temp
        self.tail=self.tail.prev
        self.tail.next=None
        temp.prev=None
mydoublelinkedlist=DoubleLinkedList(8)
mydoublelinkedlist.pop(8)
           

        