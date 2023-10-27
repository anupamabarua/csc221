def count(digit,n):
    count = 0

    while n > 0:
        digit = n % 10
        if digit == 5:
            count += 1
        n = n // 10

    print(count)

    """
      >>> count(5, 1055030250)
      3
      >>> count(9, 909)
      2
      >>> count(7, 7777)
      4
      >>> count(7, 1234)
      0
    """

if __name__ == '__main__':
    import doctest
    doctest.testmod()

