def recursion(A: int, B: int):
    if A == B:
        print(A)
        return None
    if A < B:
        print(A)
        return recursion(A+1, B)
    else:
        print(A)
        return recursion(A-1, B)


if __name__ == "__main__":
    recursion(15, 10)
