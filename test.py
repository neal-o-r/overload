from overload import overload

@overload
def add(a: int, b: int) -> int:
    return a + b


@overload
def add(a: list, b: list) -> list:
    return [ai + bi for ai, bi in zip(a, b)]


if __name__ == "__main__":

    print(add(1, 2))
    print(add([1, 2, 3], [4, 5, 6]))

