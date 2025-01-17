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

    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail.prev=self.tail
            self.tail=new_node
            self.length=+1
    def Popfirst(self,value):
        if self.length is 0 :
            return None
        temp=self.head
        if self.length==1:
            self.head=None
            self.tail=None
        else:
            self.head=self.head.next
            self.head.prev=None
            temp.next=None
mylinkedlist=DoubleLinkedList(7)
mylinkedlist.append(8)
mylinkedlist.append(9)
mylinkedlist.Popfirst()
print(mylinkedlist.Popfirst())

        