class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

def delete_tail(head):
    
    if head is None or head.next is None:
        return None

    
    temp = head

   
    while temp.next.next is not None:
        temp = temp.next

    
    temp.next = None

    
    return head


def print_ll(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next


if __name__ == "__main__":
   
    arr = [2, 5, 8, 7]

    
    head = Node(arr[0])
    head.next = Node(arr[1])
    head.next.next = Node(arr[2])
    head.next.next.next = Node(arr[3])

   
    head = delete_tail(head)

   
    print_ll(head)


