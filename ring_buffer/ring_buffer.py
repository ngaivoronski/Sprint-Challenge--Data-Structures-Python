from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.capacity > self.storage.length:
            self.storage.add_to_tail(item)
        elif self.current is None:
            self.current = self.storage.head.next
            self.storage.head.value = item
        else:
            n = self.current
            self.current.value = item
            self.current = n.next


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        curr = self.storage.head
        while curr:
            list_buffer_contents.append(curr.value)
            curr = curr.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
