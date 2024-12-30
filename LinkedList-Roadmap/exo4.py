class ListNode:
    def __init__(self, data: int, next=None):
        self.data = data 
        self.next = next 

def pushFirst(head: ListNode, val: int) -> ListNode:
    new_node = ListNode(val)
    new_node.next = head 
    return new_node 

def pushEnd(head: ListNode, val: int) -> ListNode:
    new_node = ListNode(val)
    if not head: 
        return new_node
    current = head
    while current.next:  
        current = current.next
    current.next = new_node  
    return head  
