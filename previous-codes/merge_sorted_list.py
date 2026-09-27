# merge k sorted lists
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        import heapq
        heap = []
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(heap, (l.val, i, l))
        dummy = ListNode(0)
        cur = dummy
        while heap:
            val, i, node = heapq.heappop(heap)
            cur.next = node
            cur = cur.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        return dummy.next

input1 = ListNode(1, ListNode(4, ListNode(5)))
input2 = ListNode(1, ListNode(3, ListNode(4)))
input3 = ListNode(2, ListNode(6))
q = Solution()
print(q.mergeKLists([input1, input2, input3]))