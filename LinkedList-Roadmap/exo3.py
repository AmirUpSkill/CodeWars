class ListNode:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next 
def getNth(head:ListNode,index:int)->int:
    if not head:
        return None 
    current=head
    count=0
    while current:
        if count == index:
            return current 
        count+=1
        current = current.next 
    raise ValueError("Index out of bounds ")