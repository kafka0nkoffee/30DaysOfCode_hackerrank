# Day 24: More Linked Lists

    def removeDuplicates(self, head):
        # Write your code here
        if not head:
            return head
        current = head
        while current.next:
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next
        return head
