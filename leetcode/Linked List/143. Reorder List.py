# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reorderList(head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        ptr = head
        nodes = []

        if(not head or not head.next):
            return
        while ptr:
            nodes.append(ptr)
            ptr = ptr.next
        
        for i in range((len(nodes))//2):
            nodes[i].next = nodes[len(nodes)-i-1]
            nodes[len(nodes)-i-1].next = nodes[i+1]
        
        nodes[len(nodes)//2].next = None

def test(testCases):
    for testCase in testCases:
        Solution.reorderList(head=testCase['input'])
        
        
def main():
    testCases = []
    testCase = {}
    node4 = ListNode(4)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)
    nodes = [node1, node2, node3, node4]
    testCase['input'] = node1
    testCases.append(testCase)

    test(testCases)
    
    
if __name__ == "__main__":
    main()