def even(nums):
    for n in nums:
        if n // 2 == 0:
            odd += n
        else:
            continue

    """
      
      >>> only_evens([3, 8, 5, 4, 12, 7, 2])
      [8, 4, 12, 2]
      
      >>> my_nums = [4, 7, 19, 22, 42]
      >>> only_evens(my_nums)
      [4, 22, 42]
      
      >>> my_nums
      [4, 7, 19, 22, 42]

"""

if __name__ == '__main__':
    import doctest
    doctest.testmod()
