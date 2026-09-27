# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head, k):
        def reverse_linked_list(head, k):
            new_head, ptr = None, head
            while k:
                next_node = ptr.next
                ptr.next = new_head
                new_head = ptr
                ptr = next_node
                k -= 1
            return new_head
        ptr = head
        ktail = None
        new_head = None
        while ptr:
            count = 0
            ptr = head
            while count < k and ptr:
                ptr = ptr.next
                count += 1
            if count == k:
                revHead = reverse_linked_list(head, k)
                if not new_head:
                    new_head = revHead
                if ktail:
                    ktail.next = revHead
                ktail = head
                head = ptr
        if ktail:
            ktail.next = head
        return new_head
