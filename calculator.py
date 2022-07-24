def soma(x, y):
    """
    soma x e y

    >>> soma(10, 20)
    30

    >>> soma(-10, 20)
    10

    >>> soma('10', 1)
    Traceback (most recent call last):
    ...
    AssertionError: (x) precisa ser um int ou um float
    """
    assert isinstance(x, (int, float)), '(x) precisa ser um int ou um float'
    assert isinstance(y, (int, float)), '(y) precisa ser um int ou um float'
    return x + y


def subtrai(x, y):
    """
    subrai(x, y)

    >>> subtrai(10, 6)
    4
    >>> subtrai('10', 6)
    Traceback (most recent call last):
    ...
    AssertionError: (x) precisa ser um int ou um float

    """
    assert isinstance(x, (int, float)), '(x) precisa ser um int ou um float'
    assert isinstance(y, (int, float)), '(y) precisa ser um int ou um float'
    return x - y

if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)