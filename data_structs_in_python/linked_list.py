from typing import Any


class Node:

    def __init__(self, value: Any):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def __contains__(self, value: Any) -> bool:
        last = self.head
        while last is not None:
            if last.value == value:
                return True
            last = last.next
        return False

    def __len__(self) -> int:
        count = 0
        last = self.head
        while last is not None:
            last = last.next
            count += 1
        return count

    def append(self, value: Any):
        if self.head is None:
            self.head = Node(value)
        else:
            last = self.head
            while last.next is not None:  # in the tutorial, it is 'while last.next':
                last = last.next
            last.next = Node(value)

    def delete(self, value: Any):
        if self.head is None:
            return

        last = self.head
        if last.value == value:
            self.head = last.next
        else:
            while last.next is not None:
                if last.next.value == value:
                    last.next = last.next.next
                    break

    def insert(self, value: Any, index: int):
        if index == 0:
            self.prepend(value)
        else:
            if self.head is None:
                raise IndexError('list index out of range')

            last = self.head
            for i in range(index - 1):
                if last.next is None:
                    raise IndexError('list index out of range')
                last = last.next

            new_node = Node(value)
            new_node.next = last.next
            last.next = new_node

    def prepend(self, value: Any):
        first_node = Node(value)
        first_node.next = self.head
        self.head = first_node


if __name__ == '__main__':
    pass
