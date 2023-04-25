def recursion(x: int, y=1) -> None:
    if y > x:
        return
    else:
        print(y, end=' ')
        y += 1
        return recursion(x, y)


if __name__ == "__main__":
    recursion(10)