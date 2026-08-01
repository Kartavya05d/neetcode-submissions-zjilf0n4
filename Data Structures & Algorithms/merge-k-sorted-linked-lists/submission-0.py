# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0: return None
        
        for i in range(1, len(lists)):
            lists[i] = self.mergetwolist(lists[i-1], lists[i])
        return lists[-1]

    def mergetwolist(self, p, q):
        dummy = ListNode()
        curr = dummy
        while p and q:
            if p.val < q.val:
                curr.next = p
                p = p.next
            else:
                curr.next = q
                q = q.next
            curr = curr.next
        curr.next = p if p else q
        return dummy.next
