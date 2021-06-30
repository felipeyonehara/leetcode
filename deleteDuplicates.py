# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        start = ListNode()
        current = previous = start = head
        
        if (current is not None): 
            current = current.next
        else:
            return current
        
        print(current, previous)
        
        while( current is not None):
            
            if(current.val == previous.val):
                previous.next = current.next        
                current = current.next
            else:    
                previous = current
                current = current.next
            
        return start