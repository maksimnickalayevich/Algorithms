from typing import Any, Optional


class Node:
    def __init__(self, data: Any = None, nextItem=None):
        self.data: Any = data
        self.nextItem: Node = nextItem

    def __repr__(self):
        return f"{self.data}"


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data: Any, index: int = 0):
        """
        Inserts data to the given index or, byt default to the beginning of the LinkedList
        :param data: data to insert
        :param index: index to fill
        :return:
        """
        newNode: Node = Node(data, self.head)
        self.head = newNode

    def append(self, data):
        """
        Appends data to the end of the linked list
        :param data: data to append
        :return:
        """
        # Check if LL is empty
        if not self.head:
            node = Node(data, None)
            self.head = node
            return

        # Iteration through the Ll from head
        elem: Optional[Node] = self.head
        while elem:
            if not elem.nextItem:
                lastNode = Node(data, None)
                elem.nextItem = lastNode
                break

            elem = elem.nextItem

    def remove(self, value):
        """
        Removes value from the linked list
        :param value: value to remove
        :return:
        """
        if not self.head:
            raise AttributeError(value)

        curr: Node = self.head
        while curr:
            if curr.nextItem.data == value:
                curr.nextItem = curr.nextItem.nextItem
                break
            curr = curr.nextItem

    def getLength(self) -> int:
        """
        Returns the length of the sequence
        :return:
        """
        if not self.head:
            return 0

        curr: Node = self.head
        counter: int = 0
        while curr:
            counter += 1
            curr = curr.nextItem

        return counter

    def __iter__(self):
        return self

    def __repr__(self):
        current: Optional[Node] = self.head
        strToPrint = ""
        while current:
            strToPrint += f"{current.data}"
            if current.nextItem:
                strToPrint += " --> "
            current = current.nextItem

        return strToPrint
