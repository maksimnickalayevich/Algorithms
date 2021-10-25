from typing import Optional, List, Any
from ..helpers import tmed


@tmed(template="BINARY SEARCH")
def binarySearch(source: List[Any], value: Any):
    """
    Implementation of binary search in Python
    :param source: where to search
    :param value: what to search
    :return: index of searched value
    """
    start = 0
    end = len(source)
    resultIndex: Optional[int] = None
    counter = 0

    while not resultIndex or start < end:
        half = (end - start) // 2
        assumption = source[start + half]

        if value > assumption:
            start = start + half
        elif value < assumption:
            end = end - half
        else:
            resultIndex = start + half
        counter += 1

    return resultIndex, counter


@tmed(template="DUBM SEARCH")
def dumbSearch(source: List[Any], value: Any):
    """
    Implementation of rough/dumb search by going through all the elements
    :param source: where to search
    :param value: what to search
    :return: index of searched value
    """
    result: Optional[int] = None
    for val in source:
        if val == value:
            result = source.index(val)

    return result


def populateTestList(length: int) -> List[Any]:
    newList: List[int] = []
    for i in range(length):
        newList.append(i+1)
    return newList


if __name__ == "__main__":
    testList = populateTestList(10 ** 8)
    searchDumb = dumbSearch(testList, 5 ** 4)
    searchBinary, effort = binarySearch(testList, 5 ** 4)

