# Linked List Construction
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1

my_Linked_list=LinkedList(4)
print("My linked list head value",my_Linked_list.head.value)
