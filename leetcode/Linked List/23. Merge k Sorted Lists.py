
class Solution:
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
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
        
        res = None

        while len(lists) > 1:
            i = 0
            while i < len(lists)-1:
                lists.insert(2, mergeTwoLists(lists[0], lists[1]))
                lists.pop(0)
                lists.pop(0)


        return lists[0] if len(lists) > 0 else None