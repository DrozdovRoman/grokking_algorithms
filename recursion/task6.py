def recursion(arr: list) -> int:
    if len(arr) == 1:
        return arr.pop(0)
    x = arr.pop(0)
    y = recursion(arr)
    if x < y:
        return y
    else:
        return x


test_arr = [52, 2, 67, 45, 34]

if __name__ == "__main__":
    recursion(test_arr)
