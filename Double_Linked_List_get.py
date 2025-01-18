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
    def append(self,value):
        new_node=Node(value)
        if  self.head is  None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail.prev=self.tail
            self.tail=new_node
            self.length=+1
        return true
    def get(self,value):
        if index<0 or index>=self.length:
            return None
        temp=self.head
        if index<=self.length/2:
            for _ in range(index):
                temp=temp.next
        else:
            temp=self.tail
            for _ in range(self.length-1,index,-1):
                temp=temp.prev
        return temp
    mydoublelinkedlist=DoubleLinkedList(8)
    mydoublelinkedlist.append(7)
    mydoublelinkedlist.append(9)
    mydoublelinkedlist.get(1)
    print(mydoublelinkedlist.get(1))
