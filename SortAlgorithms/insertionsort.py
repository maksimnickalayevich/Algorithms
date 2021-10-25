def insertion(to_sort):
    l = len(to_sort)
    for i in range(l):
        for j in range(i, 0, -1):
            if to_sort[j] < to_sort[j-1]:
                to_sort[j], to_sort[j-1] = to_sort[j-1], to_sort[j]
            else:
                break
    return to_sort


if __name__ == "__main__":
    arr = [5, 7, 4, 3, 8, 2, 1, 6]
    print(insertion(arr))
