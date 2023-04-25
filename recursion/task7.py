def recursion(arr: list, find: int) -> int:
    if len(arr) == 1:
        return arr.pop(0)
    x = arr.pop(0)
    y = recursion(arr)
    if x < y:
        return y
    else:
        return x


test_arr = [1, 3, 15, 25, 74]

if __name__ == "__main__":
    recursion(test_arr)
