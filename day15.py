# Day 15: Linked List

    def insert(self, head, data):
        # handle the corner case
        if not head:
            return Node(data)

        # handle the general case
        current = head
        while current.next:
            current = current.next
        current.next = Node(data)

        return head
