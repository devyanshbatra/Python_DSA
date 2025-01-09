class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class Linkedlist:
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
    
    def get(self,index):
        if index<0 or index>=self.length:
            return None
        temp=self.head
        for _ in range(index):
            temp=temp.next
        return temp
    def set(self,index,value):
        temp.self.get(index)
        if temp:
            temp.value=value
            return True
        return False
    
my_Linked_List=Linkedlist(1)
my_Linked_List.append(2)
my_Linked_List.append(3)
print(my_Linked_List.set(1,4))
