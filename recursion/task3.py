def recursion(n: int):
    if n == 1:
        print('Yes')
        return
    if n % 2 == 0:
        return recursion(n // 2)
    else:
        print('No')
        return


if __name__ == "__main__":
    recursion(32)
