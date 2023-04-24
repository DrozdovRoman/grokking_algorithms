def indSmallest(arr: list) -> int:
    smallest = arr[0]
    smallest_index = 0
    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr: list) -> list:
    result = []
    for i in range(len(arr)):
        smallest = indSmallest(arr)
        result.append(arr.pop(smallest))
    return result


if __name__ == "__main__":
    selection_sort([2, 6, 5, 7, 3])
