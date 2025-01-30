class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class Stack:
    def __init__(self,value):
        new_node=Node(value)
        self.top=new_node
        self.height=1
    def pop (self):
        if self.height is 0:
            return None
        else:
          self.top=temp
          self.top=self.top.next
          temp.next=None

my_stack=Stack(6)
my_stack.pop(6)


    