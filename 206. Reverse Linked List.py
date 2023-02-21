# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        prev = None 
        
        curr_node = head
        
        
        while curr_node :
            
            nextNode = curr_node.next 
            
            curr_node.next = prev 
            
            
            prev = curr_node 
            
            curr_node = nextNode 
            
        return prev
             
