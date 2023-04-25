def recursion(arr: list) -> int:
    if len(arr) == 0:
        return 0
    else:
        arr.pop()
        return 1 + recursion(arr)


test_arr = [1, 2, 3, 22, 34]

if __name__ == "__main__":
    print(recursion(test_arr))
