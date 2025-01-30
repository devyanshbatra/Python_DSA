class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class Queue:
    def __init__(self,value):
        new_node=Node(value)
        self.first=new_node
        self.last=new_node
        self.length=1
    def printQueue(self):
        self.first=temp
        while temp is not None:
            print(temp.value)
            temp=temp.next
    my_queue=Queue()
    print(my_queue)
