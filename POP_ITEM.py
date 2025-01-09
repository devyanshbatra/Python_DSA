class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Linked_List:
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
         self.tail=new_node

    def pop(self):
        if self.length==0:
            return None
    temp=self.head
    pre=self.head

    while(temp.next):
            pre = temp
            temp = temp.next
    self.tail = pre
    self.tail.next = None
    self.length -= 1

my_Linked_List=Linked_List(6) 
my_Linked_List.append(7)
print(my_Linked_List.pop(2))