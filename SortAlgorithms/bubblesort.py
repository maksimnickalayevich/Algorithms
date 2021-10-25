def bubble(to_sort):
    length = len(to_sort)
    interchange = 0
    attempt = 0
    while attempt < length - 1:
        for i in range(length-1):
            if to_sort[i] > to_sort[i + 1]:
                to_sort[i], to_sort[i+1] = to_sort[i+1], to_sort[i]
                interchange += 1
        attempt += 1
    return to_sort, interchange


if __name__ == "__main__":
    l = [5, 7, 4, 3, 8, 2, 1, 6]
    sorted_arr, count = bubble(l)
    print(f"{sorted_arr} : {count}")
