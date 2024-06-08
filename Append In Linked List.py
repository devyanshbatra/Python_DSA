class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Linkedlist:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
    def append(self,value):
        new_node=node(value)
        if self.head = none:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
            self.length +=1
new_linked_list=Linkedlist()
new_linked_list.append(10)
new_linked_list.append(20)
print(new_linked_list.length)
print(new_linked_list.tail.value)

