from typing import Dict, Union, Optional, List


class BiNode:
    def __init__(self, value: Union[int, float], left=None, right=None):
        self.value: Union[int, float] = value
        self.left: Optional[BiNode] = left
        self.right: Optional[BiNode] = right

    def __repr__(self):
        return f"v:{self.value} l:{self.left} - r:{self.right}"


class BiTree:
    def __init__(self, head: Optional[Union[int, float]] = None):
        self.head: Optional[Union[int, float]] = head

    def _addHead(self, value: Union[int, float]):
        self.head = BiNode(value)

    def add(self, val: Union[int, float]):
        if not self.head:
            self._addHead(val)
        else:
            self._appendNode(val, self.head)

    def _appendNode(self, value, parent: BiNode):
        if value < parent.value:
            if parent.left:
                self._appendNode(value, parent.left)
            else:
                parent.left = BiNode(value)
        else:
            if parent.right:
                self._appendNode(value, parent.right)
            else:
                parent.right = BiNode(value)

    def find(self, value):
        if self.head:
            return self._find(value, self.head)
        else:
            return None

    def _find(self, value: Union[int, float], parent: BiNode):
        if value == parent.value:
            return parent
        elif value < parent.value:
            if parent.left:
                return parent.left if parent.left.value == value else self._find(value, parent.left)
            return None
        else:
            if parent.right:
                return parent.right if parent.right.value == value else self._find(value, parent.right)
            return None


if __name__ == "__main__":
    bi = BiTree()
    bi.add(12)
    bi.add(5)
    bi.add(1)
    bi.add(2)
    bi.add(6)
    bi.add(9)
    bi.add(10)
    print(bi)
    print(bi.find(5))
