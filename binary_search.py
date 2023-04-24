def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = low + high
        temp = list[mid]

        if temp == item:
            return mid
        if temp > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

test_list = [1, 3, 5, 7, 9]

if __name__ == "__main__":
    binary_search(test_list, 3)