class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class Linkedlist:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
    
    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node


    def pop_first(self):
        if self.head is 0:
            return None
        temp=self.head
        self.head=self.head.next
        temp.next=None
        self.length-=1
        if self.length==0:
            self.tail=None
        return temp
my_Linked_List=Linkedlist(5)
my_Linked_List.append(7)
print(my_Linked_List.pop_first())