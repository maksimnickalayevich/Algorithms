from typing import List, Any, Tuple


def findSmallestValue(source: List[Any]) -> int:
    """
    Finds the smallest value in the sequence
    :param source: sequence
    :return:
    """

    smallestValue = source[0]
    smallestIndex = 0
    for i, v in enumerate(source):
        if v < smallestValue:
            smallestValue = v
            smallestIndex = i

    return smallestIndex


def selectionSort(source: List[Any]) -> List:
    """
    Selection sort of the list
    :param source: 
    :return: 
    """
    sortedArr = []
    for _ in range(len(source)):
        smIndex = findSmallestValue(source)
        sortedArr.append(source.pop(smIndex))

    return sortedArr


if __name__ == "__main__":
    smallest = findSmallestValue([5, 6, 13, 11, 8, 4, 2, 1])
    sortedArr = selectionSort([5, 6, 13, 11, 8, 4, 2, 1])
    assert smallest == 7
    assert sortedArr == [1, 2, 4, 5, 6, 8, 11, 13]
    print(f"Smallest index: {smallest}")
    print(f"Sorted arr: {sortedArr}")
