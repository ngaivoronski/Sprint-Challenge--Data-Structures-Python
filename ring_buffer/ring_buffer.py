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
        self.capacity = capacity
        self.current = 0
        self.storage = [None for i in range(capacity)]

    def append(self, item):
        if self.current < self.capacity:
            self.storage[self.current] = item
            self.current += 1
        else:
            self.storage[0] = item
            self.current = 1

    def get(self):
        return [element for element in self.storage if element != None]
