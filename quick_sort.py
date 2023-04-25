def quick_sort(arr: list):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [element for element in arr[1:] if element < pivot]
        greater = [element for element in arr[1:] if element > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


test_arr = [44, 15, 22, 51, 2]

if __name__ == "__main__":
    quick_sort(test_arr)
