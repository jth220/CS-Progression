# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Function to get the middle node of the linked list
        def getMiddle(head):
            slow = head
            fast = head
            while fast.next is not None and fast.next.next is not None:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        # Function to merge two sorted linked lists
        def merge(a, b):
            dummy = ListNode()
            tail = dummy
            while a and b:
                if a.val <= b.val:
                    tail.next = a
                    a = a.next
                else:
                    tail.next = b
                    b = b.next
                tail = tail.next
            # Attach the remaining part
            if a:
                tail.next = a
            if b:
                tail.next = b
            return dummy.next
        
        # Function to recursively split and sort the linked list
        def mergeAndSort(head):
            if head is None or head.next is None:
                return head
            
            middle = getMiddle(head)
            next_to_middle = middle.next
            middle.next = None

            left = mergeAndSort(head)
            right = mergeAndSort(next_to_middle)

            sortedlist = merge(left, right)
            return sortedlist

        return mergeAndSort(head)
