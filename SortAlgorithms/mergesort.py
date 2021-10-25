def merge_lists(l1, l2):
    new_list = []
    i = j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            new_list.append(l1[i])
            i += 1
        else:
            new_list.append(l2[j])
            j += 1
    if i < len(l1):
        new_list += l1[i:]
    if j < len(l2):
        new_list += l2[j:]
    return new_list


def mergesort(to_sort):
    if len(to_sort) == 1:
        return to_sort
    mid = len(to_sort) // 2
    left = mergesort(to_sort[:mid])
    right = mergesort(to_sort[mid:])
    return merge_lists(left, right)


if __name__ == "__main__":
    arr = [5, 8, 3, 1, 19, 7, 6, 9, 4, 10, 11]  # 1, 3, 4, 5, 6, 7, 8, 9, 10, 11,19
    print(*mergesort(arr))
