# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = res = ListNode()
        while list1 and list2:
            if list2.val <= list1.val:
                merged.next = list2
                merged = merged.next
                list2 = list2.next
            else:
                merged.next = list1
                merged = merged.next
                list1 = list1.next
        
        merged.next = list1 if list1 else list2 if list2 else None
        
        return res.next
        