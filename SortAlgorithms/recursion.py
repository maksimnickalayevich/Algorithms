from copy import deepcopy
from typing import List, Union, Any


def rSum(list_to_sum: List[Union[int, float]]):
    """
    Sum of all values in the list calculated with recursion
    :param list_to_sum: list of values to sum
    :return:
    """
    if not len(list_to_sum):
        return 0
    list_copy = deepcopy(list_to_sum)
    if len(list_copy) == 1:
        return list_copy[0]

    return list_copy.pop() + rSum(list_copy)


def rLen(list_of_elems: List[Any]):
    """
    Counts the number of items in the list recursively
    :param list_of_elems:
    :return:
    """
    total_count: int = 1
    if not list_of_elems:
        return 0
    new_list = deepcopy(list_of_elems)
    new_list.pop()
    return total_count + rLen(new_list)


def searchMax(list_to_search: List[Union[int, float]]):
    """
    Finds the maximum value in the list recursively
    :param list_to_search:
    :return:
    """
    if not len(list_to_search):
        return 0
    new_list = deepcopy(list_to_search)
    max_value = new_list.pop()
    max_value = max_value if max_value > searchMax(new_list) else searchMax(new_list)
    return max_value


if __name__ == "__main__":
    testList = [2, 4, 6, 5]
    print(rSum(testList))
    print(rSum([]))
    print(rLen(testList))
    print(searchMax([1, 2, 3, 4, 5, 13, 10, 15, 11, 33, 23, 56, 10]))
