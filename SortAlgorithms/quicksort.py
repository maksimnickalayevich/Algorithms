from typing import Any, List


def quicksort(list_to_sort: List[Any]):
    """
    Uses divide and conquer strategy to implement quicksort
    :param list_to_sort:
    :return:
    """
    if len(list_to_sort) < 2:
        return list_to_sort

    foundation: Any = list_to_sort[0]
    smaller: List[Any] = [sm for sm in list_to_sort if sm < foundation]
    greater: List[Any] = [gt for gt in list_to_sort if gt > foundation]
    return quicksort(smaller) + [foundation] + quicksort(greater)


if __name__ == "__main__":
    testList: List[int] = [3, 5, 1, 9, 2, 11, 19, 114, 52, 21, 10, 12]
    sortedList = quicksort(testList)
    print(sortedList)
    assert [1, 2, 3, 5, 9, 10, 11, 12, 19, 21, 52, 114] == sortedList
